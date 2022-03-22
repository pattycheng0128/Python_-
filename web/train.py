import requests
from bs4 import BeautifulSoup
import time

url = "https://tip.railway.gov.tw"
staDic = {} # 找到火車站的相關資訊存在這個字典內
today = time.strftime("%Y/%m/%d")
sTime = '06:00'
eTime = '23:59'

def getTrip():
  resp = requests.get(url + '/tra-tip-web/tip')
  if resp.status_code != 200:
    print("URL發生錯誤" + url)
    return
  
  soup = BeautifulSoup(resp.text, 'html5lib')
  stations = soup.find(id='cityHot').ul.find_all('li')
  for station in stations:
    stationName = station.button.text
    stationId = station.button['title']
    staDic[stationName] = stationId
    
  csrf = soup.find(id='queryForm').find('input', {'name': '_csrf'})['value']
  
  # 在 network 抓到 querybytime 的 Form data 資訊
  formData = {
    'trainTypeList' : "ALL",
    'transfer': 'ONE',
    'startOrEndTime': 'true',
    'startStation': staDic['臺北'],
    'endStation': staDic['高雄'],
    'rideDate': today,
    'startTime': sTime,
    'endTime': eTime,
    '_csrf': csrf
  }
  
  queryUrl = soup.find(id='queryForm')['action']
  qResp = requests.post(url + queryUrl, data=formData)
  qSoup = BeautifulSoup(qResp.text, 'html5lib')
  trs = qSoup.find_all('tr', 'trip-column')
  for tr in trs:
      td = tr.find_all('td')
      print('%s : %s, %s' % (td[0].ul.li.a.text, td[1].text, td[2].text))     
  

getTrip()