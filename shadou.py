# -*- coding: utf8 -*-
import requests

BOOK = 1
MOVIE = 2
MUSIC = 3

class ShaDou(object):
    u"豆瓣帐号信息复制"

    def __init__(self):
        self.books = []
        self.movies = []
        self.music = []

    def getInfo(self, type=BOOK):
        ret = requests.get("https://api.douban.com/v2/book/1220562")
        print ret

    def login(self)
        pass


if __name__ == "__main__":
    ret = ShaDou()
    ret.getInfo()
