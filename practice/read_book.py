from urllib import request
import configparser


def read_book(book_path,headers):
    http = request(
        
    )


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('/Users/liuhailong/VscodeProjects/pyCode/python_study/config.ini')
    book_path = config.get('Book','shaosong')
    headers={
            'Cookie':'__gads=ID=c89a49c625723d6e-22017b571acb0056:T=1629787759:RT=1629787759:S=ALNI_MZxcW3MDqUPJ-YKEw4wghr2rEq50w; Hm_lpvt_cec763d47d2d30d431932e526b7f1218=1629787759; Hm_lvt_cec763d47d2d30d431932e526b7f1218=1629787705; PHPSESSID=f7rr24em39u2qppcjguqmqnsg1; jieqiUserInfo=jieqiUserId%3D71729%2CjieqiUserUname%3Dliulian0001%2CjieqiUserName%3Dliulian0001%2CjieqiUserGroup%3D3%2CjieqiUserGroupName%3D%C6%D5%CD%A8%BB%E1%D4%B1%2CjieqiUserVip%3D0%2CjieqiUserHonorId%3D%2CjieqiUserHonor%3D%D6%D0%BC%B6%BB%E1%D4%B1%2CjieqiUserPassword%3Da0621265fd9d6629066119a09961a5fe%2CjieqiUserUname_un%3Dliulian0001%2CjieqiUserName_un%3Dliulian0001%2CjieqiUserHonor_un%3D%26%23x4E2D%3B%26%23x7EA7%3B%26%23x4F1A%3B%26%23x5458%3B%2CjieqiUserGroupName_un%3D%26%23x666E%3B%26%23x901A%3B%26%23x4F1A%3B%26%23x5458%3B%2CjieqiUserLogin%3D1629787758; jieqiVisitId=article_articleviews%3D100580; jieqiVisitInfo=jieqiUserLogin%3D1629787758%2CjieqiUserId%3D71729',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate, br',
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15',
            'Accept-Language':'zh-cn',
            'Connection':'keep-alive'
        }
    read_book(book_path,headers)