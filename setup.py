#!/usr/bin/env python

# Remove .egg-info directory if it exists, to avoid dependency problems with
# partially-installed packages (20160119/dphiffer)

import os, sys
from shutil import rmtree

cwd = os.path.dirname(os.path.realpath(sys.argv[0]))
egg_info = cwd + "/mapzen.whosonfirst.uri.egg-info"
if os.path.exists(egg_info):
    rmtree(egg_info)

from setuptools import setup, find_packages

packages = find_packages()
version = open("VERSION").read()
desc = open("README.md").read()

setup(
    name='mapzen.whosonfirst.uri',
    python_requires='>3',
    namespace_packages=['mapzen', 'mapzen.whosonfirst'],
    version=version,
    description='Shared utilities for working with URIs for Who\'s On First documents',
    author='Mapzen',
    url='https://github.com/whosonfirst/py-mapzen-whosonfirst-uri',
    packages=packages,
    scripts=[
        "scripts/wof-id2path"
        ],
    download_url='https://github.com/whosonfirst/py-mapzen-whosonfirst-uri/releases/tag/' + version,
    license='BSD')
