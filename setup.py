# -*- coding: utf-8 -*-
#

import os

from setuptools import find_packages, setup

extras_require = {
    'tests': [
        'click==7.1.2',
        'pytest==4.6.11',
        'six==1.16.0',
    ]
}

setup_requires = [
    'pytest-runner>=3.0.0,<5',
]

install_requires = [
    'click==7.1.2',
    'six==1.16.0',
    'sqlalchemy==1.3.24',
    'py-postgresql',
]

# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join('app', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name='app',
    version=version,
    entry_points={
        'console_scripts': ['app=app.main:go'],
    },
    packages=find_packages()
)
