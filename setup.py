from typing import Tuple

from setuptools import (
    setup,
    find_packages,
)


requirements: Tuple[str, ...] = (
    'setuptools',
    'networkx',
)


setup(
    name='textrankr',
    version='1.1',
    license='MIT',
    author='Jamie Seol',
    author_email='theeluwin@gmail.com',
    url='https://github.com/theeluwin/textrankr',
    description="TextRank implemented in Python.",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    classifiers=[]
)
