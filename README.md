# textrankr

[![Build Status](https://travis-ci.org/theeluwin/textrankr.svg?branch=master)](https://travis-ci.org/theeluwin/textrankr)
[![Coverage Status](https://coveralls.io/repos/github/theeluwin/textrankr/badge.svg?branch=master)](https://coveralls.io/github/theeluwin/textrankr?branch=master)
[![PyPI version](https://badge.fury.io/py/textrankr.svg)](https://badge.fury.io/py/textrankr)

Reorder sentences using the [TextRank](http://digital.library.unt.edu/ark:/67531/metadc30962/) algorithm.

* Mostly designed for Korean, but not limited to.
* Check out [lexrankr](https://github.com/theeluwin/lexrankr), which is an another awesome summarizer!
* Not available for Python 2 anymore (if necessary, use version 0.3).

## Installation

```bash
pip install textrankr
```

## Tokenizers

Tokenizers are not included. You have to implement it by yourself.

Example:

```python
from typing import List

class MyTokenizer:
    def __call__(self, text: str) -> List[str]:
        tokens: List[str] = text.split()
        return tokens
```

한국어의 경우 [KoNLPy](http://konlpy.org)를 사용하는 방법이 있습니다. 아래 예시처럼 `phrases`를 쓰게되면 엄밀히는 토크나이저가 아니지만 이게 더 좋은 결과를 주는것 같습니다.

```python
from typing import List
from konlpy.tag import Okt

class OktTokenizer:
    okt: Okt = Okt()

    def __call__(self, text: str) -> List[str]:
        tokens: List[str] = self.okt.phrases(text)
        return tokens
```

## Usage

```python
from typing import List
from textrankr import TextRank

mytokenizer: MyTokenizer = MyTokenizer()
textrank: TextRank = TextRank(mytokenizer)

k: int = 3  # num sentences in the resulting summary

summarized: str = textrank.summarize(your_text_here, k)
print(summarized)  # gives you some text

# if verbose=False, it returns a list
summaries: List[str] = textrank.summarize(your_text_here, k, verbose=False)
for summary in summaries:
    print(summary)
```

## Test

Use docker.

```bash
docker build -t textrankr -f Dockerfile .
docker run textrankr
```
