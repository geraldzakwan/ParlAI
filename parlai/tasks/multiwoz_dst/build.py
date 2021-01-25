#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
# Download and build the data if it does not exist.

import parlai.core.build_data as build_data
import os
from parlai.core.build_data import DownloadableFile

RESOURCES = [
    DownloadableFile(
        'https://github.com/geraldzakwan/conv_dataset/blob/main/trade-dst/train_dials.json?raw=true',
        'train_dials.json',
        'a61cc5e618b2c0708e9f5ec2bf63676a84b0b0ed2f1d893b6d13ed4d11262ce8',
        zipped=False,
    ),
    DownloadableFile(
        'https://github.com/geraldzakwan/conv_dataset/blob/main/trade-dst/dev_dials.json?raw=true',
        'dev_dials.json',
        '28bb7fa64e62b385df5828bdaecdcd2a62b4f3f11385a41d2e75f2afa43274b8',
        zipped=False,
    ),
    DownloadableFile(
        'https://github.com/geraldzakwan/conv_dataset/blob/main/trade-dst/test_dials.json?raw=true',
        'test_dials.json',
        '708bd57234242e562cd238f6e95df282ca30e721d8e2e6e1f03e4c10d0dff249',
        zipped=False,
    ),
]


def build(opt):
    dpath = os.path.join(opt['datapath'], 'multiwoz_dst')
    version = '1.0'

    if not build_data.built(dpath, version_string=version):
        print('[building data: ' + dpath + ']')
        if build_data.built(dpath):
            build_data.remove_dir(dpath)
        build_data.make_dir(dpath)

        # Download the data.
        for downloadable_file in RESOURCES:
            downloadable_file.download_file(dpath)

        build_data.mark_done(dpath, version_string=version)
