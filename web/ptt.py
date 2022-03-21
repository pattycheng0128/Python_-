import requests
from bs4 import BeautifulSoup
import time


# 取得日期後,用 lstrip 將左邊的0做刪除
today = time.strftime('%m/%d').lstrip('0')

def ptt_nba(url):
  resp = requests.get(url)
  if resp.status_code != 200:
    print("URL發生錯誤" + url)
    return
  
  soup = BeautifulSoup(resp.text, 'html5lib')
  # 取得上頁元素
  paging = soup.find('div', 'btn-group btn-group-paging').find_all('a')[1]['href']
  
  articles = []
  
  # 取得所有文章的 title, 推文數, 日期
  rents = soup.find_all('div', 'r-ent')
  for rent in rents:
    title = rent.find('div', 'title').text.strip() # strip 去除首尾的空白
    count = rent.find('div', 'nrec').text.strip()
    date = rent.find('div', 'meta').find('div', 'date').text.strip()
    article = '%s %s:%s' % (date, count, title)
    
    try:
      if today == date and int(count) > 10:
        articles.append(article)
    except:
      if today == date and count == "爆":
        articles.append(article)
        
  if len(articles) > 0:
    for article in articles:
      print(article)
      

url = 'https://www.ptt.cc/bbs/NBA/index.html'
ptt_nba(url)

