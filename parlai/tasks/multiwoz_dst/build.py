#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
# Download and build the data if it does not exist.

import parlai.core.build_data as build_data
import os
from parlai.core.build_data import DownloadableFile

# schema.json, dialog_acts.json, 17 dialogue files for train, 2 for dev and test
RESOURCES = [
    DownloadableFile(
        'https://raw.githubusercontent.com/budzianowski/multiwoz/master/data/MultiWOZ_2.2/schema.json',
        'schema.json',
        'ae9e2390f38fb967af64623c2f4f7e0c636fb377ad523b582a03161d3ddbdf68',
        zipped=False,
    ),
    DownloadableFile(
        'https://raw.githubusercontent.com/budzianowski/multiwoz/master/data/MultiWOZ_2.2/dialog_acts.json',
        'dialog_acts.json',
        '1f51ac200dcf8154aeee37e3a9fea3ee9d6fa5b111208de55ded74d39d82bafa',
        zipped=False,
    ),
    DownloadableFile(
        'https://raw.githubusercontent.com/budzianowski/multiwoz/raw/master/data/MultiWOZ_2.2/train/dialogues_001.json',
        'train/dialogues_001.json',
        'd5558cd419c8d46bdc958064cb97f963d1ea793866414c025906ec15033512ed',
        zipped=False,
    ),
    DownloadableFile(
        'https://raw.githubusercontent.com/budzianowski/multiwoz/raw/master/data/MultiWOZ_2.2/train/dialogues_002.json',
        'train/dialogues_002.json',
        'd5558cd419c8d46bdc958064cb97f963d1ea793866414c025906ec15033512ed',
        zipped=False,
    ),
    DownloadableFile(
        'https://raw.githubusercontent.com/budzianowski/multiwoz/raw/master/data/MultiWOZ_2.2/train/dialogues_003.json',
        'train/dialogues_003.json',
        'd5558cd419c8d46bdc958064cb97f963d1ea793866414c025906ec15033512ed',
        zipped=False,
    ),
    DownloadableFile(
        'https://raw.githubusercontent.com/budzianowski/multiwoz/raw/master/data/MultiWOZ_2.2/train/dialogues_004.json',
        'train/dialogues_004.json',
        'd5558cd419c8d46bdc958064cb97f963d1ea793866414c025906ec15033512ed',
        zipped=False,
    ),
    DownloadableFile(
        'https://raw.githubusercontent.com/budzianowski/multiwoz/raw/master/data/MultiWOZ_2.2/train/dialogues_005.json',
        'train/dialogues_005.json',
        'd5558cd419c8d46bdc958064cb97f963d1ea793866414c025906ec15033512ed',
        zipped=False,
    ),
    DownloadableFile(
        'https://raw.githubusercontent.com/budzianowski/multiwoz/raw/master/data/MultiWOZ_2.2/train/dialogues_006.json',
        'train/dialogues_006.json',
        'd5558cd419c8d46bdc958064cb97f963d1ea793866414c025906ec15033512ed',
        zipped=False,
    ),
    DownloadableFile(
        'https://raw.githubusercontent.com/budzianowski/multiwoz/raw/master/data/MultiWOZ_2.2/train/dialogues_007.json',
        'train/dialogues_007.json',
        'd5558cd419c8d46bdc958064cb97f963d1ea793866414c025906ec15033512ed',
        zipped=False,
    ),
    DownloadableFile(
        'https://raw.githubusercontent.com/budzianowski/multiwoz/raw/master/data/MultiWOZ_2.2/train/dialogues_008.json',
        'train/dialogues_008.json',
        'd5558cd419c8d46bdc958064cb97f963d1ea793866414c025906ec15033512ed',
        zipped=False,
    ),
    DownloadableFile(
        'https://raw.githubusercontent.com/budzianowski/multiwoz/raw/master/data/MultiWOZ_2.2/train/dialogues_009.json',
        'train/dialogues_009.json',
        'd5558cd419c8d46bdc958064cb97f963d1ea793866414c025906ec15033512ed',
        zipped=False,
    ),
    DownloadableFile(
        'https://raw.githubusercontent.com/budzianowski/multiwoz/raw/master/data/MultiWOZ_2.2/train/dialogues_010.json',
        'train/dialogues_010.json',
        'd5558cd419c8d46bdc958064cb97f963d1ea793866414c025906ec15033512ed',
        zipped=False,
    ),
    DownloadableFile(
        'https://raw.githubusercontent.com/budzianowski/multiwoz/raw/master/data/MultiWOZ_2.2/train/dialogues_011.json',
        'train/dialogues_011.json',
        'd5558cd419c8d46bdc958064cb97f963d1ea793866414c025906ec15033512ed',
        zipped=False,
    ),
    DownloadableFile(
        'https://raw.githubusercontent.com/budzianowski/multiwoz/raw/master/data/MultiWOZ_2.2/train/dialogues_012.json',
        'train/dialogues_012.json',
        'd5558cd419c8d46bdc958064cb97f963d1ea793866414c025906ec15033512ed',
        zipped=False,
    ),
    DownloadableFile(
        'https://raw.githubusercontent.com/budzianowski/multiwoz/raw/master/data/MultiWOZ_2.2/train/dialogues_013.json',
        'train/dialogues_013.json',
        'd5558cd419c8d46bdc958064cb97f963d1ea793866414c025906ec15033512ed',
        zipped=False,
    ),
    DownloadableFile(
        'https://raw.githubusercontent.com/budzianowski/multiwoz/raw/master/data/MultiWOZ_2.2/train/dialogues_014.json',
        'train/dialogues_014.json',
        'd5558cd419c8d46bdc958064cb97f963d1ea793866414c025906ec15033512ed',
        zipped=False,
    ),
    DownloadableFile(
        'https://raw.githubusercontent.com/budzianowski/multiwoz/raw/master/data/MultiWOZ_2.2/train/dialogues_015.json',
        'train/dialogues_015.json',
        'd5558cd419c8d46bdc958064cb97f963d1ea793866414c025906ec15033512ed',
        zipped=False,
    ),
    DownloadableFile(
        'https://raw.githubusercontent.com/budzianowski/multiwoz/raw/master/data/MultiWOZ_2.2/train/dialogues_016.json',
        'train/dialogues_016.json',
        'd5558cd419c8d46bdc958064cb97f963d1ea793866414c025906ec15033512ed',
        zipped=False,
    ),
    DownloadableFile(
        'https://raw.githubusercontent.com/budzianowski/multiwoz/raw/master/data/MultiWOZ_2.2/train/dialogues_017.json',
        'train/dialogues_017.json',
        'd5558cd419c8d46bdc958064cb97f963d1ea793866414c025906ec15033512ed',
        zipped=False,
    ),
    DownloadableFile(
        'https://raw.githubusercontent.com/budzianowski/multiwoz/raw/master/data/MultiWOZ_2.2/dev/dialogues_001.json',
        'dev/dialogues_001.json',
        'd5558cd419c8d46bdc958064cb97f963d1ea793866414c025906ec15033512ed',
        zipped=False,
    ),
    DownloadableFile(
        'https://raw.githubusercontent.com/budzianowski/multiwoz/raw/master/data/MultiWOZ_2.2/dev/dialogues_002.json',
        'dev/dialogues_002.json',
        'd5558cd419c8d46bdc958064cb97f963d1ea793866414c025906ec15033512ed',
        zipped=False,
    ),
    DownloadableFile(
        'https://raw.githubusercontent.com/budzianowski/multiwoz/raw/master/data/MultiWOZ_2.2/test/dialogues_001.json',
        'test/dialogues_001.json',
        'd5558cd419c8d46bdc958064cb97f963d1ea793866414c025906ec15033512ed',
        zipped=False,
    ),
    DownloadableFile(
        'https://raw.githubusercontent.com/budzianowski/multiwoz/raw/master/data/MultiWOZ_2.2/test/dialogues_002.json',
        'test/dialogues_002.json',
        'd5558cd419c8d46bdc958064cb97f963d1ea793866414c025906ec15033512ed',
        zipped=False,
    ),
]


def build(opt):
    dpath = os.path.join(opt['datapath'], 'multiwoz_v22')
    version = '1.0'

    if not build_data.built(dpath, version_string=version):
        print('[building data: ' + dpath + ']')
        if build_data.built(dpath):
            build_data.remove_dir(dpath)
        build_data.make_dir(dpath)

        # Train, dev and test dir
        build_data.make_dir(os.path.join(dpath, 'train'))
        build_data.make_dir(os.path.join(dpath, 'dev'))
        build_data.make_dir(os.path.join(dpath, 'test'))

        # Download the data.
        for downloadable_file in RESOURCES:
            downloadable_file.download_file(dpath)

        build_data.mark_done(dpath, version_string=version)
