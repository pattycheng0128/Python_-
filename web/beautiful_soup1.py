import requests
from bs4 import BeautifulSoup

resp = requests.get("https://tw.yahoo.com/")
soup = BeautifulSoup(resp.text, 'html5lib')
print(soup.find('h1').text)
print(soup.h1.text)

# 用 find_all
for h1 in soup.find_all("h1"):
  print(h1.text)
  

# 用 class 取得網頁中元素資料
for b in soup.find_all('button', 'carousel-indicators'):
  print(b)

# 用 key-value 取得網頁中的元素

# 抓取文章標題和資訊
for posts in soup.find_all('div', 'C(#fff)'):
  # print(posts)
  for post in posts.stripped_strings:
    print(post)