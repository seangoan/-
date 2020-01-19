import requests
from bs4 import BeautifulSoup
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
headers = {'User-Agent': user_agent}
url = 'https://www.ptt.cc/bbs/movie/index.html'

###訪問 3 個頁面
for p in range(0,3):
    print(url)
    res = requests.get(url, headers=headers)

    # print(res.text)
    # 轉成BeautifulSoup型態
    soup = BeautifulSoup(res.text, 'html.parser')
    # print(soup)

    title = soup.select('div[class="title"]')

    for n, t in enumerate(title):
        #print(t)
        title_name = t.text
        title_url = 'https://www.ptt.cc' + t['href']
        ####文章存檔.py
        res_article = requests.get(title.url)
        soup_article = BeautifulSoup(res_article.text, 'html.parser')
        article_content = soup_article.select('div[id="main-content"]')
        all_article = article_content[0].text
        article_part = all_article.split('--')[0]
        f = open(r'./resource/test_%s_%s.txt'%(p,n), 'w', encoding='utf-8')
        f.write(article_part)
        f.close()
        print(title_name)
        print(title_url)
        print()

### 取得上頁的網址
last_page_url = soup.select('a[class="btn wide"]')
new_url = 'https://wwww.ptt.cc' + last_page_url[1]['href']
url = new_url
# print('https://www.ptt.cc' + last_page_url[1]['href']

