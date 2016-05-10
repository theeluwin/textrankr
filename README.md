TextRank for Korean
==========

Reorder sentences using [TextRank][1] algorithm.
Click [here][2] to see how to install [KoNLPy][3] properly.


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
