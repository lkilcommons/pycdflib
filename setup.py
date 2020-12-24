# Copyright 2018 SEDA Group at CU Boulder
# Created by:
# Liam Kilcommons
# Space Environment Data Analysis Group (SEDA)
# Colorado Center for Astrodynamics Research (CCAR)
# University of Colorado, Boulder (CU Boulder)
import os
import glob

os.environ['DISTUTILS_DEBUG'] = "1"

from setuptools import setup, Extension
from setuptools.command import install as _install

setup(name='pycdflib',
      version = "0.1",
      description = "Pythonic interface for CDF file I/O with cdflib",
      author = "Liam Kilcommons",
      author_email = 'liam.kilcommons@colorado.edu',
      url = "https://github.com/lkilcommons/pycdflib",
      download_url = "https://github.com/lkilcommons/pycdflib",
      long_description = \
            """This package provides a more pythonic
            interface to cdflib, similar to spacepy.pycdf. 
            I made it to avoid having to adapt legacy code 
            which originally used spacepy.pycdf 
            (which requires painful manual installation) to cdflib, which 
            can be installed with pip (more Cloud / CI friendly)
            """,
      install_requires=['numpy','cdflib'],
      tests_require=['requests','pytest'],
      packages=['pycdflib'],
      package_dir={'pycdflib' : 'pycdflib'}, 
      license='LICENSE.txt',
      zip_safe = False,
      classifiers = [
            "Development Status :: 3 - Alpha",
            "Topic :: Scientific/Engineering",
            "Intended Audience :: Science/Research",
            "Natural Language :: English",
            "Programming Language :: Python"
            ],
      )