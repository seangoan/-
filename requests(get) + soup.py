import requests
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'

headers = {'User-Agent': user_agent}

url = 'https://www.ptt.cc/bbs/movie/index.html'

res = requests.get(url, headers=headers)

# print(res.text)
# 轉成BeautifulSoup型態
soup = BeautifulSoup(res.text, 'html.parser')
print(soup)

