#-*- coding: utf-8 -*-
from urllib import request

if __name__ == '__main__':
    url = 'http://www.baidu.com'
    head = {}
    head['User-Agent'] = 'User-Agent:Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us)\
         AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
    req = request.Request(url, headers=head)
    response = request.urlopen(req)
    html = response.read().decode('utf-8')
    print(html)