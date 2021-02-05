#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from parlai.core.loader import register_teacher
from parlai.core.teachers import DialogTeacher
from parlai.core.metrics import AverageMetric, ExactMatchMetric
from parlai.utils.io import PathManager
from .build import build

import json
import os

@register_teacher("multiwoz_dst")
class MultiWozDstTeacher(DialogTeacher):
    """
    MultiWOZ 2.2 Teacher.
    """

    # Standard initialization for an Agent
    def __init__(self, opt, shared=None):
        # Initialize datatype, the value is one of these:
        # ["train", "valid", "test"]
        self.datatype = opt['datatype']

        # Mandatory function to call for an Agent in its initialization
        build(opt)

        # Choose JSON file based on datatype
        suffix = 'train'
        if opt['datatype'].startswith('valid') or opt['datatype'].startswith('dev'):
            suffix = 'dev'
        elif opt['datatype'].startswith('test'):
            suffix = 'test'

        # Load the file
        self.jsons_path = os.path.join(opt['datapath'], 'multiwoz_dst')
        opt['datafile'] = os.path.join(self.jsons_path, '{}_dials.json'.format(suffix))

        # Set the task ID
        self.id = 'multiwoz_dst'

        # Call parent Initialization
        super().__init__(opt, shared)

        # Flag for joint goal accuracy metric
        self.complete_match = True

    # To load and parse the JSON file
    def setup_data(self, path):
        """
        Load json data of conversations.
        """
        # Note that 'path' is the value provided by opt['datafile']
        print('Loading: ' + path)

        with PathManager.open(path) as data_file:
            self.dialogues = json.load(data_file) # Load a list of dialogues

        for dialogue in self.dialogues: # Dialogue is a dict
            # dialogue_id is the filename excluding .json extension
            dialogue_id = dialogue['dialogue_idx'][:len(dialogue['dialogue_idx'])-4]

            # The code below is to parse the dialog dict inside the JSON file
            for idx, turn in enumerate(dialogue['dialogue']):
                # I am adding two more fields: 'first_turn' and 'last_turn'
                # that I use when computing joint goal accuracy

                first_turn = False
                if turn['turn_idx'] == 0:
                    new_episode = True

                last_turn = False
                if idx == len(dialogue['dialogue']) - 1:
                    last_turn = True

                if len(turn['turn_label']) == 0:
                    # This is when the belief state is empty,
                    # I am using 'default:none' as the label in this case
                    yield {
                        'text': turn['transcript'],
                        'labels': ['default:none'],
                        'first_turn': first_turn,
                        'last_turn': last_turn,
                    }, new_episode
                else:
                    yield {
                        'text': turn['transcript'],
                        'labels': [':'.join(turn_label) for turn_label in turn['turn_label']],
                        'first_turn': first_turn,
                        'last_turn': last_turn,
                    }, new_episode

    # To define joint goal accuracy metric
    def custom_evaluation(
        self, teacher_action, labels, model_response
    ) -> None:
        if 'text' not in model_response:
            # No response from the model, skip this example
            return

        teacher_text = teacher_action['text']
        model_text = model_response['text']

        # Check the flag whether or not we've reached the end of the dialog
        if not teacher_action['last_turn']:
            # If not, we update our flag, i.e.
            # set it to False if model and teacher have different responses
            # Otherwise, set keep it as True
            if ExactMatchMetric.compute(model_text, teacher_text) == 0:
                self.complete_match = False
        else:
            # We reach the end of the dialog
            if self.complete_match:
                # If the flag is still True we give the model a point
                self.metrics.add('joint_goal_acc', AverageMetric(1, 1))
            else:
                # Otherwise, we give zero point
                self.metrics.add('joint_goal_acc', AverageMetric(0, 1))

            # Reset the flag to True to get ready for the next dialog
            self.complete_match = True


class DefaultTeacher(MultiWozDstTeacher):
    pass
