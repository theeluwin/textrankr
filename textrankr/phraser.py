# -*- coding: utf-8 -*-

from konlpy.tag import Okt
import requests
import json


class OktPhraser(object):

    okt = Okt()

    def phrases(self, text):
        return self.okt.phrases(text)


class ApiPhraser(object):

    def __init__(self, api_url):
        self.api_url = api_url

    def phrases(self, text):
        r = requests.post(self.api_url, data=text.encode('utf-8'))
        return json.loads(r.text)
