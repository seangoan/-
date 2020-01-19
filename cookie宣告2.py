import requests

from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'

headers = {'User-Agent': user_agent}

url = 'https://www.ptt.cc/bbs/movie/M.1578413203.A.1DB.html'

### 宣告cookie
ss = requests.session()
ss.cookies['over18'] = '1'

res = ss.get(url, headers=headers)
c = ss.cookies.get_dict()

soup = BeautifulSoup(res.text, 'html.parser')

print(soup)