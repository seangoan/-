import requests
from bs4 import BeautifulSoup
user_agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Mobile Safari/537.36'
headers = {'User-Agent': user_agent}
url = 'https://www.backpackers.com.tw/forum/forumdisplay.php?f=60'

res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text, 'html.parser')

article_content = soup.select('div[style="padding:0px 0px 0px 0px"]')
all_article = article_content[0].text
article_part = all_article.split('--')[0]
print(article_part)

f = open(r'./test.txt', 'w', encoding='utf-8')
f.write(article_part)
f.close()

