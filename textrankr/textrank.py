from typing import (
    List,
    Dict,
    Tuple,
    Union,
    Callable,
)

from networkx import (
    Graph,
    pagerank,
)

from .utils import (
    parse_text_into_sentences,
    build_sentence_graph,
)
from .sentence import Sentence


__all__: Tuple[str, ...] = (
    'TextRank',
)


class TextRank:
    """
        Args:
            tokenizer: a function or a functor of Callable[[str], List[str]] type.
            tolerance: a threshold for omitting edge weights.

        Example:
            ```
            tokenizer: YourTokenizer = YourTokenizer()
            textrank: TextRank = TextRank(tokenzier, tolerance=0.05)
            summaries: str = textrank.summarize(your_text_here, num_sentences=True, verbose=True)
            print(summaries)
            ```
    """

    def __init__(self, tokenizer: Callable[[str], List[str]], tolerance: float = 0.05) -> None:
        self.tokenizer: Callable[[str], List[str]] = tokenizer
        self.tolerance: float = tolerance

    def summarize(self, text: str, num_sentences: int = 3, verbose: bool = True) -> Union[str, List[str]]:
        """
            Summarizes the given text, using TextRank algorithm.

            Args:
                text: a raw text to be summarized.
                num_sentences: the number of sentences in a summarization result.
                verbose: if True, it will return a summarized raw text. It will return a summarized list of sentences otherwise.
        """

        # parse text
        sentences: List[Sentence] = parse_text_into_sentences(text, self.tokenizer)

        # build graph
        graph: Graph = build_sentence_graph(sentences, tolerance=self.tolerance)

        # run pagerank
        pageranks: Dict[Sentence, float] = pagerank(graph, weight='weight')

        # get top-k sentences
        sentences = sorted(pageranks, key=pageranks.get, reverse=True)
        sentences = sentences[:num_sentences]
        sentences = sorted(sentences, key=lambda sentence: sentence.index)

        # return summaries
        summaries = [sentence.text for sentence in sentences]
        if verbose:
            return '\n'.join(summaries)
        else:
            return summaries
