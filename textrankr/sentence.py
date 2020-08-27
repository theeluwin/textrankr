# -*- coding: utf-8 -*-

from collections import Counter


class Sentence(object):

    def __init__(self, phraser, text, index=0):
        self.index = index
        self.text = text.strip()
        self.tokens = phraser(self.text)
        self.bow = Counter(self.tokens)

    def __str__(self):
        return self.text

    def __hash__(self):
        return self.index
