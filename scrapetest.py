from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle():
    try:
        html = urlopen('http://www.baidu.com')
    except HTTPError as e:
        print('链接异常')
    try:
        bsObj = BeautifulSoup(html.read(),'html.parser')
        title = bsObj.title
    except AttributeError as e:
        print('标签异常')
    return title

title = getTitle()
print(title)