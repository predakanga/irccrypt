#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.md').read()

setup(
    name='irccrypt',
    version='0.1.1',
    description='Library containing IRC encryption functions',
    long_description=readme,
    author='Björn Edström',
    author_email='be@bjrn.se',
    url='https://github.com/predakanga/irccrypt',
    packages=[
        'irccrypt',
    ],
    package_dir={'irccrypt': 'irccrypt'},
    include_package_data=True,
    install_requires=['pycrypto'],
    license="BSD",
    zip_safe=True,
    keywords='irccrypt',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)