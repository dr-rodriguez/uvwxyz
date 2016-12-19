#! /usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
    setup
except ImportError:
    from distutils.core import setup
    setup

setup(name='uvwxyz',
      version='1.1.1',
      description='Calculate XYZ and UVW coordinates',
      url='https://github.com/dr-rodriguez/uvwxyz.git',
      author='David Rodriguez',
      author_email='drodriguez1@amnh.org',
      license='MIT',
      install_requires=['numpy', 'astropy'],
      packages=['uvwxyz'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python'
      ],
      keywords='astrophysics',
      )
