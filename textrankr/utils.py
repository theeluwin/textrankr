from typing import (
    List,
    Tuple,
    Callable,
)

from re import split
from itertools import combinations
from collections import Counter

from networkx import Graph

from .sentence import Sentence


__all__: Tuple[str, ...] = (
    'parse_text_into_sentences',
    'multiset_jaccard_index',
    'build_sentence_graph',
)


def parse_text_into_sentences(text: str, tokenizer: Callable[[str], List[str]]) -> List[Sentence]:
    """
        This function splits the given text into sentence candidates using a pre-defined splitter,
        then creates a list of `sentence.Sentence` instances which have bag-of-words inside, tokenized by the given tokenizer.
    """

    # init
    index: int = 0
    duplication_checker: set = set()
    sentences: List[Sentence] = []

    # parse text
    candidates: List[str] = split(r'(?:(?<=[^0-9])\.|\n|!|\?)', text)
    for candidate in candidates:

        # cleanse the candidate
        candidate_stripped: str = candidate.strip('. ')
        if not len(candidate_stripped):
            continue
        if candidate_stripped in duplication_checker:
            continue

        # tokenize the candidate
        tokens: List[str] = tokenizer(candidate_stripped)
        if len(tokens) < 2:
            continue
        duplication_checker.add(candidate_stripped)

        # create a sentence
        bow: Counter = Counter(tokens)
        sentence = Sentence(index, candidate_stripped, bow)
        sentences.append(sentence)
        index += 1

    # return
    return sentences


def multiset_jaccard_index(counter1: Counter, counter2: Counter) -> float:
    """
        Calculates the jaccard index between two given multisets.
        Note that a `Counter` instance can be used for representing multisets.
    """
    intersection_count: int = sum((counter1 & counter2).values())
    union_count: int = sum((counter1 | counter2).values())
    try:
        return intersection_count / union_count
    except ZeroDivisionError:
        return 0.0


def build_sentence_graph(sentences: List[Sentence], tolerance: float = 0.05) -> Graph:
    """
        Builds a `networkx.Graph` instance, using sentences as nodes.
        An edge weight is determined by the jaccard index between two sentences,
        but the edge will be ignored if the weight is lower then the given tolerance.
    """

    # init
    graph: Graph = Graph()

    # add nodes
    graph.add_nodes_from(sentences)

    # add edges
    for sentence1, sentence2 in combinations(sentences, 2):
        weight: float = multiset_jaccard_index(sentence1.bow, sentence2.bow)
        if weight > tolerance:
            graph.add_edge(sentence1, sentence2, weight=weight)

    # return
    return graph
