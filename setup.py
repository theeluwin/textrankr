# -*- coding: utf-8 -*-

import os
import warnings

from setuptools import setup
from setuptools import find_packages


requirements = [
    'setuptools',
    'networkx',
    'konlpy',
]

if os.name == 'nt':
    warnings.warn("See http://konlpy.org/en/latest/install/#id2 to properly install KoNLPy.", RuntimeWarning)


setup(
    name='textrankr',
    version='0.6',
    license='MIT',
    author='Jamie Seol',
    author_email='theeluwin@gmail.com',
    url='https://github.com/theeluwin/textrankr',
    description='TextRank for Korean',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    classifiers=[]
)
