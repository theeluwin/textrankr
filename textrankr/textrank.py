from typing import List
from typing import Dict
from typing import Callable

from networkx import Graph
from networkx import pagerank

from .sentence import Sentence

from .utils import parse_text_into_sentences
from .utils import build_sentence_graph


class TextRank:
    """
        Args:
            tokenizer: a function or a functor of Callable[[str], List[str]] type.
            tolerance: a threshold for omitting edge weights.

        Example:
            tokenizer: YourTokenizer = YourTokenizer()
            textrank: TextRank = TextRank(tokenzier)
            summaries: str = textrank.summarize(your_text_here)
            print(summaries)
    """

    def __init__(self, tokenizer: Callable[[str], List[str]], tolerance: float = 0.05) -> None:
        self.tokenizer: Callable[[str], List[str]] = tokenizer
        self.tolerance: float = tolerance

    def summarize(self, text: str, num_sentences: int = 3, verbose: bool = True):
        """
            Summarizes the given text, using the textrank algorithm.

            Args:
                text: a raw text to be summarized.
                num_sentences: number of sentences in the summarization results.
                verbose: if True, it will return a summarized raw text, otherwise it will return a list of sentence texts.
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
