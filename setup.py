#!/usr/bin/env python

from setuptools import setup

setup(
  name='pychemy',
  version='0.3.0',

  author='Benjie Chen, Ginkgo Bioworks, Christoph Gohlke',
  author_email='benjie@ginkgobioworks.com, devs@ginkgobioworks.com, cgohlke@uci.edu',

  description='Helpers for handling chemical formulas in Python',
  long_description=open('README.rst').read(),
  url='https://github.com/ginkgobioworks/pychemy',

  license='MIT',
  keywords='chemistry mass spectrometry chemoinformatics analysis molecular',
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Environment :: Other Environment',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2.7',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'Topic :: Scientific/Engineering :: Artificial Life',
    'Topic :: Scientific/Engineering :: Bio-Informatics',
    'Topic :: Scientific/Engineering :: Chemistry',
    'Topic :: Scientific/Engineering :: Information Analysis',
    'Topic :: Scientific/Engineering :: Mathematics',
    'Topic :: Scientific/Engineering :: Visualization',
    'Topic :: Software Development :: Libraries :: Python Modules',
  ],

  packages=['pychemy'],
  include_package_data=True,
  zip_safe=True,

  install_requires=[
    'matplotlib',
    'networkx',
    'numpy',
    'openbabel',
  ],
  tests_require=[
    'tox',
    'nose',
    'coverage',
  ],
)
