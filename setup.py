from setuptools import find_packages, setup

setup(
    name='textrankr',
    version='0.2',
    license='MIT',
    author='Jamie Seol',
    author_email='theeluwin@gmail.com',
    url='https://github.com/theeluwin/textrankr',
    description='TextRank for Korean',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['setuptools', 'networkx', 'konlpy', 'jpype1'],
    classifiers=[],
)
