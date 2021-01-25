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

        self.jsons_path = os.path.join(opt['datapath'], 'multiwoz_dst', 'MULTIWOZ2.2')

        self.schema_path = os.path.join(self.jsons_path, 'schema.json')
        self.dialog_acts_path = os.path.join(self.jsons_path, 'dialog_acts.json')

        self.train_path = os.path.join(self.jsons_path, 'train')
        self.dev_path = os.path.join(self.jsons_path, 'dev')
        self.test_path = os.path.join(self.jsons_path, 'test')

        opt['datafile'] = os.path.join(self.train_path, 'dialogues_001.json')
        self.id = 'multiwoz_dst'
        super().__init__(opt, shared)

    def _setup_data(self, schema_path, dialog_acts_path, train_path, dev_path, test_path):
        pass

class DefaultTeacher(MultiWozDstTeacher):
    pass
