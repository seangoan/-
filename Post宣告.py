import requests
from bs4 import BeautifulSoup
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
headers = {'User-Agent':user_agent}

url = 'http://64b7860a.ngrok.io/homework_all/DB105'

# Post宣告
post_data = {'pew':'REIxMDU=', '_hidden_info':'471829599'}
cookies = {'class_id':'DB105', 'hidden_code':'1572765333'}
#post_data2 = [('username', 'sssssss')]
#post_data3 = {'location' : '中壢'}

res = requests.post(url, data=post_data, cookies=cookies)

soup = BeautifulSoup(rest.text, 'html.parser')

print(soup)


##### 若開發人員工具出現cookie & form data，二者皆需要帶入
