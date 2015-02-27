# -*- coding: utf8 -*-
from douban_client import DoubanClient
import requests

# 首次获取的图书信息数
COUNT = 100

API_KEY = '01270ca17245f891037525e456d1e9b3'
API_SECRET = 'c4732649acfecebb'
#API_KEY = '09d2c50567d6e5491d784f103784afdb'
#API_SECRET = 'c194f8fccc17a325'
REDIRECT_URI = 'http://jzguo.com/callback_dou'
# 权限设置
SCOPE = 'douban_basic_common,book_basic_r,book_basic_w'

class ShaDou(object):
    u"豆瓣图书信息迁移"

    def __init__(self):
        self.books = []
        self.movies = []
        self.music = []
        self.client = None
        self.books = None

    def _saveBooks(self, books):
        data = books.get('collections')
        self.books.extend(data)

    def getAllBooks(self):
        u"保存原账户读书信息"
        user_from = raw_input('please input your original username:')
        start = 0
        self.books = []
        ret = self.client.book.getAllBooks(user_from, start, COUNT)
        self._saveBooks(ret)
        total = int(ret.get('total', 0))
        start = start+int(ret.get('count', 0))
        total = total-int(ret.get('count', 0))
        while total>0:
            ret = self.client.book.getAllBooks(user_from, start, total)
            total = total-int(ret.get('count', 0))
            start = start+int(ret.get('count', 0))
            self._saveBooks(ret)

    def setAllBooks(self):
        u"设置新账户读书信息"
        left = len(self.books)
        while self.books:
            print left, 'book[s] left'
            book = self.books.pop()
            param = {}
            param['status'] = book['status']
            param['comment'] = book.get('comment', '')
            param['tags'] = ' '.join(book.get('tags', []))
            param['rating'] = int(book.get('rating', {}).get('value', 0))
            self.client.book.newBook(book['book_id'], param)
            left = left-1

    def login(self):
        self.client = None
        self.client = DoubanClient(API_KEY, API_SECRET, REDIRECT_URI, SCOPE)
        print 'Go to the following link in your browser:' 
        print self.client.authorize_url
        code = raw_input('Enter the verification code:')
        self.client.auth_with_code(code)

    def migrate(self):
        self.login()
        self.getAllBooks()
        self.login()
        self.setAllBooks()


if __name__ == "__main__":
    toy = ShaDou()
    toy.migrate()
