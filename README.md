TextRank for Korean
==========

Reorder sentences using [TextRank][1] algorithm.
Click [here][2] to see how to install [KoNLPy][3] properly.

Upgraded version named [lexrankr][4] using [LexRank][5] is available too!

Installation
-----

```sh
pip install textrankr
```

Usage
-----

```python
from __future__ import print_function
from textrankr import TextRank

textrank = TextRank(your_text_here)
print(textrank.summarize())
```


Test
-----

```bash
python -m tests.test
```

[1]: http://digital.library.unt.edu/ark:/67531/metadc30962/
[2]: http://konlpy.org/en/latest/install/
[3]: http://konlpy.org/
[4]: https://github.com/theeluwin/lexrankr
[5]: http://dl.acm.org/citation.cfm?id=1622501
