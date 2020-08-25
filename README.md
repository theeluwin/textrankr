# TextRank for Korean

[![Build Status](https://travis-ci.org/theeluwin/textrankr.svg?branch=master)](https://travis-ci.org/theeluwin/textrankr)
[![Coverage Status](https://coveralls.io/repos/github/theeluwin/textrankr/badge.svg?branch=master)](https://coveralls.io/github/theeluwin/textrankr?branch=master)
[![PyPI version](https://badge.fury.io/py/textrankr.svg)](https://badge.fury.io/py/textrankr)

Reorder sentences using [TextRank](http://digital.library.unt.edu/ark:/67531/metadc30962/) algorithm.
Click [here](http://konlpy.org/en/latest/install/) to see how to install [KoNLPy](http://konlpy.org/) properly (you'll need some java stuff).

Check out [lexrankr](https://github.com/theeluwin/lexrankr), which is another awesome summarizer!

Not available for Python 2 anymore (if necessary, use version 0.3).

## Installation

```bash
pip install textrankr
```

## Usage

```python
from textrankr import TextRank

textrank = TextRank(your_text_here)
print(textrank.summarize())  # gives you some text
print(textrank.summarize(3, verbose=False))  # up to 3 sentences, returned as list
```

## Test

Testing requires some additional packages (`flake8` is optional, though).

```bash
pip install nose nose-exclude flake8 coverage
```

Test with [nose](https://nose.readthedocs.io/).

```bash
nosetests --config=.noserc
```

Or, you can use docker.

```bash
docker build -t textrankr -f Dockerfile .
docker run textrankr
```
