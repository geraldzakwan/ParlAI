#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from parlai.core.teachers import DialogTeacher
from parlai.utils.io import PathManager
from .build import build

import json
import os


class MultiWozDstTeacher(DialogTeacher):
    """
    MultiWOZ 2.2 Teacher.
    """

    def __init__(self, opt, shared=None):
        self.datatype = opt['datatype']
        build(opt)

        suffix = 'train'
        if opt['datatype'].startswith('dev'):
            suffix = 'dev'
        elif opt['datatype'].startswith('test'):
            suffix = 'test'

        self.jsons_path = os.path.join(opt['datapath'], 'multiwoz_dst')
        opt['datafile'] = os.path.join(self.jsons_path, '{}_dials.json'.format(suffix))

        self.id = 'multiwoz_dst'
        super().__init__(opt, shared)

    def setup_data(self, path):
        """
        Load json data of conversations.
        """
        # Note that path is the value provided by opt['datafile']
        print('Loading: ' + path)

        with PathManager.open(path) as data_file:
            self.dialogues = json.load(data_file) # Load a list of dialogues

        for dialogue in self.dialogues: # dialogue is a dict
            # dialogue_id is the filename excluding .json extension
            dialogue_id = dialogue['dialogue_idx'][:len(dialogue['dialogue_idx'])-4]

            for cnt, turn in enumerate(dialogue['dialogue']):
                new_episode = False

                if cnt == 0:
                    new_episode = True

                if len(turn['turn_label']) == 0:
                    yield {
                        'text': turn['transcript'],
                        'labels': ['default:none'],
                    }, new_episode
                else:
                    yield {
                        'text': turn['transcript'],
                        'labels': [':'.join(turn_label) for turn_label in turn['turn_label']],
                    }, new_episode

                # yield {
                #     'text': turn['system_transcript'] + '\n' + turn['transcript'],
                #     'labels': 'DUMMY', # a list
                #     # 'labels': turn['turn_label'], # a list
                #     'id': dialogue_id,
                #     'system_transcript': turn['system_transcript'],
                #     'transcript': turn['transcript'],
                #     'turn_idx': turn['turn_idx'],
                #     'belief_state': turn['belief_state'],
                #     'turn_label': turn['turn_label'],
                #     'system_acts': turn['system_acts'],
                #     'domain': turn['domain'],
                # }, new_episode


class DefaultTeacher(MultiWozDstTeacher):
    pass
