# -*- coding: utf-8 -*-

import json
import requests

from typing import List

from konlpy.tag import Okt
from requests.models import Response


class OktTokenizer:
    """
        A POS-tagger based tokenizer functor. Note that these are just an examples. Using phrases function rather than a mere POS tokenizer seems better.

        Example:
            tokenizer: OktTokenizer = OktTokenizer()
            tokens: List[str] = tokenizer(your_text_here)
    """

    okt: Okt = Okt()

    def __call__(self, text: str) -> List[str]:
        tokens: List[str] = self.okt.phrases(text)
        return tokens


class ApiTokenizer:
    """
        An API based tokenizer functor, assuming that the response body is a jsonifyable string with content of list of str tokens.

        Example:
            tokenizer: ApiTokenizer = ApiTokenizer()
            tokens: List[str] = tokenizer(your_text_here)
    """

    def __init__(self, endpoint: str) -> None:
        self.endpoint: str = endpoint

    def __call__(self, text: str) -> List[str]:
        body: bytes = text.encode('utf-8')
        res: Response = requests.post(self.endpoint, data=body)
        tokens: List[str] = json.loads(res.text)
        return tokens
