#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from setuptools import setup
from setuptools import find_packages

setup(
    name='wazo_call_logd_client',
    version='1.0',

    description='a simple client library for the wazo-call-logd HTTP interface',

    author='Wazo Authors',
    author_email='dev@wazo.community',

    url='http://wazo.community',

    packages=find_packages(),

    entry_points={
        'wazo_call_logd_client.commands': [
            'cdr = wazo_call_logd_client.commands.cdr:CDRCommand',
        ],
    }
)
