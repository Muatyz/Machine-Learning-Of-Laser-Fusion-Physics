#引入包
import requests
from bs4 import BeautifulSoup

#身份信息
#添加headers
headers={'User-Agent':'Mozilla/5.0(iPhone;CPU iPhone OS 11_0 like Mac OS X)AppleWebKit'}
#post请求
data={'users':'abc','password':'123'}

#保持会话
#新建对象
sess=requests.session()
#登陆
sess.post('login_url',data=data,headers=headers)
#在会话下访问网址
sess.get('other_urls')

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
# 选用lxml解析器来解析
soup = BeautifulSoup(html, 'lxml')
