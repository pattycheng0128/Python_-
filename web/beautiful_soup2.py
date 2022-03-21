import requests
from bs4 import BeautifulSoup

# 透過 requests.get 去確認 response 回來的狀態
resp = requests.get("https://code-gym.github.io/spider_demo/")
# print(resp.status_code)
# 透過 BeautifulSoup 去分析網頁的 HTML 與 XML 文件
soup = BeautifulSoup(resp.text, 'html5lib')
# print(soup)

nav = soup.find(id='nav')
print(nav)

# 取得 nav 的父母親元素- parent
header = nav.parent
print(header)

# 尋找平行的兄弟姐妹節點- previous_sibling, next_sibling
javascript = soup.find('li', 'cat-2')
print("自己", javascript)
print("前一個節點", javascript.previous_sibling)
print("下一個節點", javascript.next_sibling)

# 抓取小孩節點 children
ul = soup.find('ul')
print(ul)
for li in ul.children:
  print(li.find('a'))
