# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages


requirements = [
    'setuptools',
    'networkx',
    'jpype1-py3',
    'konlpy',
]

setup(
    name='textrankr',
    version='0.4',
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
