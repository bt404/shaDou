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
SCOPE = 'douban_basic_common,movie_basic,movie_basic_r,movie_basic_w,thing_basic_r,\
         thing_basic_w,book_basic_r,book_basic_w,music_basic_r,music_basic_w,music_artist_r'

class ShaDou(object):
    u"豆瓣帐号信息复制"

    def __init__(self):
        self.books = []
        self.movies = []
        self.music = []
        self.client = None

    def getInfo(self, type=BOOK):
        ret = requests.get("https://api.douban.com/v2/book/1220562")
        print ret

    def login(self):
        self.client = DoubanClient(API_KEY, API_SECRET, REDIRECT_URI, SCOPE)
        print 'Go to the following link in your browser:' 
        print client.authorize_url
        code = raw_input('Enter the verification code:')
        self.client.auth_with_code(code)


if __name__ == "__main__":
    client = DoubanClient(API_KEY, API_SECRET, REDIRECT_URI, SCOPE)
    print 'Go to the following link in your browser:' 
    print client.authorize_url
    code = raw_input('Enter the verification code:')
    client.auth_with_code(code)

    #ret = client.book.getMyBook('25857804')

    param = {}
    param['status'] = 'read'
    param['tags'] = 'efficience learning'
    param['comment'] = 'a good self-learning book'
    param['rating'] = '4'

    ret = client.book.newBook('26297606', param)
    print ret
