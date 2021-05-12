"""
在Pytho2.x中使用import urllib2——-对应的，在Python3.x中会使用import urllib.request，urllib.error。
在Pytho2.x中使用import urllib——-对应的，在Python3.x中会使用import urllib.request，urllib.error，urllib.parse。
在Pytho2.x中使用import urlparse——-对应的，在Python3.x中会使用import urllib.parse。
在Pytho2.x中使用import urlopen——-对应的，在Python3.x中会使用import urllib.request.urlopen。
在Pytho2.x中使用import urlencode——-对应的，在Python3.x中会使用import urllib.parse.urlencode。
在Pytho2.x中使用import urllib.quote——-对应的，在Python3.x中会使用import urllib.request.quote。
在Pytho2.x中使用cookielib.CookieJar——-对应的，在Python3.x中会使用http.CookieJar。
在Pytho2.x中使用urllib2.Request——-对应的，在Python3.x中会使用urllib.request.Request.
"""

from urllib import request,error
import re
import configparser


def read_book(book_path):
    res = request.urlopen(book_path)
    if res.status == 200:
        content = res.read().decode('GBK')
        title = re.findall(r"<title.*?>(.+?)</title>",content)
        text = re.findall(r'<div id="content" name="content">(.+?)</div>',content)
        a = re.findall(r'>章节目录</a><a href="(.+?)" id="link-next">下一章</a>',content)
        text_str = ''.join(text)
        a_str = ''.join(a)
        text_str = text_str.replace('<br><br>&nbsp;&nbsp;&nbsp;&nbsp;','\n\n')
        text_str = text_str.replace('<br /><br /> &nbsp;&nbsp;&nbsp;&nbsp;','\n\n')
        print(title)
        print(text_str)
        print(a_str)
        config.set('Book','book_path',a_str)
        config.write(open('/Users/liuhailong/VscodeProjects/pyCode/python_study/config.ini','r+',encoding='utf-8'))
    


def open_menu(self):
    pass


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('/Users/liuhailong/VscodeProjects/pyCode/python_study/config.ini')
    book_path = config.get('Book','book_path')
    read_book(book_path)