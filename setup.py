#!/usr/bin/env python

from os.path import exists
from setuptools import setup, find_packages

from smalluuid import __version__

setup(
    name='smalluuid',
    version=__version__,
    # Your name & email here
    author='Adam Charnock',
    author_email='adam@adamcharnock.com',
    # If you had smalluuid.tests, you would also include that in this list
    packages=find_packages(
        'smalluuid.tests',
    ),
    # Any executable scripts, typically in 'bin'. E.g 'bin/do-something.py'
    scripts=[],
    url='https://github.com/adamcharnock/smalluuid',
    license='BSD',
    description="Provides ShortUUID which extends Python's builtin UUID class",
    # Any requirements here, e.g. "Django >= 1.1.1"
    install_requires=[
        
    ],
)
