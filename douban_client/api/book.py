# -*- coding: utf-8 -*-

from .subject import Subject


class Book(Subject):

    target = 'book'

    def __repr__(self):
        return '<DoubanAPI Book>'

    def isbn(self, isbn_id):
        return self._get('/v2/book/isbn/%s' % isbn_id)

    def getBook(self, book_id):
        u"获取自己对指定图书的收藏信息"
        return self._get('/v2/book/%s/collection' % book_id)

    def newBook(self, book_id, param):
        u"设置自己对指定图书的收藏"
        try:
            return self._post('/v2/book/%s/collection' % book_id, **param)
        except:
            return self._put('/v2/book/%s/collection' % book_id, **param)

    def getAllBooks(self, uid, start, count):
        u"获取自己所有图书收藏信息"
        return self._get('/v2/book/user/%s/collections?start=%s&count=%s' % (uid, start, count))
