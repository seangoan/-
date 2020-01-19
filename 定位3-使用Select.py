from urllib import request

from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Mobile Safari/537.36'

headers = {'User-Agent': user_agent}

url = 'https://www.backpackers.com.tw/forum/forumdisplay.php?f=177'

req = request.Request(url = url, headers = headers)

res = request.urlopen(req)

tmp_html = res.read().decode('utf-8')

soup = BeautifulSoup(tmp_html, 'html.parser')

#### 使用select 定位 logo
logo = soup.select('img[src="https://tw.bbkz.net/forum/images/bbkzbtns/bbkz_logo_m.png"]')
print(logo)

#### 請用select 定位 title
title = soup.select('a[class="subject"]')
print(title[0].text)


