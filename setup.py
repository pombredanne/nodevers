#!/usr/bin/env python
# coding=utf-8

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import sys
import os
import nodevers

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()

requirements = []
if sys.version_info[:2] < (2, 7):
    requirements.append("argparse")

setup(
    name='nodevers',
    version=nodevers.__version__,
    packages=['nodevers'],
    license='BSD (3-Clause) License',
    entry_points={
        'console_scripts': [
            'nodevers = nodevers.cli:main'
        ]
    },
    url='https://github.com/keremc/nodevers',
    author='Kerem Çakırer',
    author_email='kcakirer@hotmail.com',
    long_description=open("README.rst").read(),
    description='Node.js version manager',
    install_requires=requirements,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development",
        "Topic :: Utilities"
        ]
    )
