from typing import List

from setuptools import setup
from setuptools import find_packages


requirements: List[str] = [
    'setuptools',
    'networkx',
]


setup(
    name='textrankr',
    version='0.7',
    license='MIT',
    author='Jamie Seol',
    author_email='theeluwin@gmail.com',
    url='https://github.com/theeluwin/textrankr',
    description='TextRank implemented in Python',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    classifiers=[]
)
