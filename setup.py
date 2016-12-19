#! /usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
    setup
except ImportError:
    from distutils.core import setup
    setup

from uvwxyz import __version__

setup(name='uvwxyz',
      version=__version__,
      description='Calculate XYZ and UVW coordinates',
      url='https://github.com/dr-rodriguez/uvwxyz.git',
      author='David Rodriguez',
      author_email='drodriguez1[at]amnh.org',
      license='MIT',
      packages=['numpy', 'astropy', 'math'],
      install_requires=['numpy', 'astropy']
      )
