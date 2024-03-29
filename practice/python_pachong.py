"""
在Pytho2.x中使用import urllib2—�?-对应的，在Python3.x中会使用import urllib.request，urllib.error�?
在Pytho2.x中使用import urllib—�?-对应的，在Python3.x中会使用import urllib.request，urllib.error，urllib.parse�?
在Pytho2.x中使用import urlparse—�?-对应的，在Python3.x中会使用import urllib.parse�?
在Pytho2.x中使用import urlopen—�?-对应的，在Python3.x中会使用import urllib.request.urlopen�?
在Pytho2.x中使用import urlencode—�?-对应的，在Python3.x中会使用import urllib.parse.urlencode�?
在Pytho2.x中使用import urllib.quote—�?-对应的，在Python3.x中会使用import urllib.request.quote�?
在Pytho2.x中使用cookielib.CookieJar—�?-对应的，在Python3.x中会使用http.CookieJar�?
在Pytho2.x中使用urllib2.Request—�?-对应的，在Python3.x中会使用urllib.request.Request.
"""
from urllib import request
import re
import configparser
from bs4 import BeautifulSoup

def read_book(book_path,headers):
    req = request.Request(url=book_path,headers=headers)
    res = request.urlopen(req)
    print(res.read().encode('gbk'))
    if res.status == 200:
        content = res.read()
        title = re.findall(r"<title.*?>(.+?)</title>",content)
        text = re.findall(r'<div id="content" name="content">(.+?)</div>',content)
        a = re.findall(r'>章节目录</a><a href="(.+?)" id="link-next">下一章?</a>',content)
        text_str = ''.join(text)
        a_str = ''.join(a)
        text_str = text_str.replace('<br><br>&nbsp;&nbsp;&nbsp;&nbsp;','\n\n')
        text_str = text_str.replace('<br /><br /> &nbsp;&nbsp;&nbsp;&nbsp;','\n\n')
        print(title)
        print(text_str)
        print(a_str)
        config.set('Book','book_path',a_str)
        config.write(open('/Users/liuhailong/VscodeProjects/pyCode/python_study/config.ini','r+',encoding='utf-8'))


def read_book2(book_path,headers):
    res = request.urlopen(book_path,headers)
    print(res.text)
    if res.status == 200:
        bsObj = BeautifulSoup(res.read().decode('utf-8'),'html.parser',from_encoding='iso-8859-1')
        content = bsObj.find(id="content")
        print(repr(content.text))
        txt = content.text.replace('&nbsp;&nbsp;&nbsp;&nbsp;','\n    ')
        print(txt)
        # print(bsObj)
        xiayizhang = bsObj.findAll('a',href=True,text=re.compile('下一�?'))
        for link in xiayizhang:
            print(link['href'])
            config.set('Book','conghongyuekaishi','http://www.bswtan.com/75/75195/'+link['href'])
            config.write(open('/Users/liuhailong/VscodeProjects/pyCode/python_study/config.ini','r+',encoding='utf-8'))

def open_menu(self):
    pass


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('/Users/liuhailong/VscodeProjects/pyCode/python_study/config.ini')
    book_path = config.get('Book','shaosong')
    # read_book(book_path)
    headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, br',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15',
        'Accept-Language':'zh-cn',
        'Connection':'keep-alive'
    }
    read_book(book_path,headers)



print(202010%100) 