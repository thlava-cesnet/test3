# -*- coding: utf-8 -*-
#

import os

from setuptools import find_packages, setup

from Cython.Build import cythonize

EXCLUDE_FILES = [
  'app/main.py'
]

def get_ext_paths(root_dir, exclude_files):
    """get filepaths for compilation"""
    paths = []
    for root, dirs, files in os.walk(root_dir):
        for filename in files:
            if os.path.splitext(filename)[1] != '.py':
                continue
            file_path = os.path.join(root, filename)
            if file_path in exclude_files:
                continue
            paths.append(file_path)
    return paths

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
    packages=find_packages(),
    ext_modules=cythonize(
        get_ext_paths('app', EXCLUDE_FILES),
        compiler_directives={ 'language_level': 3 }
    )
)
