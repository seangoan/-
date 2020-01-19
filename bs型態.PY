from urllib import request

##
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'

headers = {'User-Agent': user_agent}

url = 'https://www.ptt.cc/bbs/movie/index.html'

req = request.Request(url = url, headers = headers)

res = request.urlopen(req)

tmp_html = res.read().decode('utf-8')

##變更為BeautifulSoup型態
soup = BeautifulSoup(tmp_html, 'html.parser')

print(soup)




