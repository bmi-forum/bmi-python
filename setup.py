#! /usr/bin/env python
from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages


setup(name='basic-modeling-interface',
      version='0.1.0',
      author='CSDMS',
      author_email='csdms@colorado.edu',
      license='MIT',
      description='Python bindings for the Basic Modeling Interface',
      long_description=open('README.md').read(),
      packages=find_packages(),
)
