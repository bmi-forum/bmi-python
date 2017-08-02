#! /usr/bin/env python
from setuptools import setup, find_packages
from basic_modeling_interface import __version__


setup(name='basic-modeling-interface',
      version=__version__,
      author='Eric Hutton',
      author_email='eric.hutton@colorado.edu',
      url='https://github.com/bmi-forum/bmi-python',
      license='MIT',
      description='Python bindings for the Basic Modeling Interface',
      long_description=open('README.md').read(),
      keywords='BMI model coupling',
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
      ],
      packages=find_packages(),
)
