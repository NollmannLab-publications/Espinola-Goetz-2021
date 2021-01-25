#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 16:18:17 2020

@author: marcnol
"""

from setuptools import setup, find_packages
from datetime import datetime

with open("README.md", "r") as fh:
    long_description = fh.read()
    
version = "0.4" + datetime.now().strftime("%Y/%m/%d %H:%M:%S")

setup(
    name='pyHiM',
    version=version,
    description='pipeline and functions to analyze Hi-M adata',
    license='MIT',
    packages=find_packages(),
    author='Marcelo Nollmann',
    author_email='marcelo.nollmann@cbs.cnrs.fr',
    keywords=['roipoly',
              'scaleogram',
              'opencv-python',
              'progress',
              'astropy',
              'photutils',
              'tqdm',
              'numpy',
              'matplotlib',
              'scikit-image',
              'stardist',
              'csbdeep',
              'tensorflow',
              'dask',
              'numba'
              'tox'
              ],
    python_requires='>=3.6.0',
    install_requires=[''],
    url='https://github.com/marcnol/pyHiM'
)


#################### to package ######################
# python3 setup.py sdist bdist_wheel

#################### to install ######################
# pip install pyHiM-0.4.0.tar.gz

