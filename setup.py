# -*- coding: utf-8 -*-
#

import os

from setuptools import find_packages, setup

# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join('test1', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name='test1',
    version=version,
    packages=find_packages()
)
