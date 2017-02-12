#!/usr/bin/env python

import os
from setuptools import setup, find_packages

settings = dict()

CLASSIFIERS = [
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'License :: Other/Proprietary License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Topic :: Utilities',
]

with open('README.md') as file_readme:
    readme = file_readme.read()

PACKAGE_NAME = "testawscode"
settings.update(
    name=PACKAGE_NAME,
    version="0.0.1",
    packages=find_packages(),
    package_data={PACKAGE_NAME:['conf/*']},
    zip_safe=False,  # force setuptools to install this as a dir instead of zip
    description="awstest",
    long_description=readme,
    license='Proprietary',
    classifiers=CLASSIFIERS
)

setup(**settings)
