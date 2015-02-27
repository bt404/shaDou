# -*- coding: utf8 -*-
from douban_client import DoubanClient
import requests

USERFROM = "knd2"
USERTO = "bt404"
BOOK = 1
MOVIE = 2
MUSIC = 3

API_KEY = '01270ca17245f891037525e456d1e9b3'
API_SECRET = 'c4732649acfecebb'
REDIRECT_URI = 'http://jzguo.com/callback_dou'
SCOPE = 'movie_basic,movie_basic_r,movie_basic_w,thing_basic_r,
         thing_basic_w,book_basic_r,book_basic_w,music_basic_r,
         music_basic_w,music_artist_r'

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
        client = DoubanClient(API_KEY, API_SECRET, REDIRECT_URI, SCOPE)


if __name__ == "__main__":
    ret = ShaDou()
    ret.getInfo()
