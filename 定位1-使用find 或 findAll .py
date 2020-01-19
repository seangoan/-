from urllib import request

from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'

headers = {'User-Agent': user_agent}

url = 'https://www.ptt.cc/bbs/movie/index.html'

req = request.Request(url = url, headers = headers)

res = request.urlopen(req)

tmp_html = res.read().decode('utf-8')

soup = BeautifulSoup(tmp_html, 'html.parser')

#print(soup)

##findAll定位
logo = soup.findAll('a', {'id':'logo'})

#string 和 text 擇一使用
print(logo[0].string)
print(logo[0].text)

#title定位
title = soup.findAll('div', {'class' : 'title'})
print(title[0])

#取出其中的標題
title_str = title[0].findAll('a')
print(title_str[0].text)
#取出標題的網址
print('http://www.ptt.cc' + title_str[0]['href'])
print()

#取出每個標題的網址
for t in title:
    each_title = t.findAll('a')[0]
    print(each_title.text)
    print('https://www.ptt.cc' + each_title['href'])
    print()




