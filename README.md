# 豆瓣搬家

`shaDou := sha[dow]Dou[ban]`

## 功能

复制已有豆瓣帐号图书信息到新豆瓣帐号。

## 操作步骤

1. 修改 USERFROM 为原账户用户名，执行 `python shadou.py`；

2. 复制网址到浏览器，输入原账户用户名密码信息并授权；

3. 复制新网址到浏览器，输入新账户用户名密码并授权。

## 注意

引用了豆瓣官方 Python 客户端 douban\_client，修改了 api/book.py 文件，添加了 `getBook`, `newBook` 和 `getAllBooks` 方法。

## TODO

1. 因请求格式不同，暂时只实现图书信息迁移，可进一步考虑实现电影/音乐信息迁移；

2. 代码增固；

3. 考虑到收藏顺序，暂时使用单线程。
