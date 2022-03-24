from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

url = "https://tw.yahoo.com/"
options = webdriver.ChromeOptions()
options.add_argument("--headless")

s = Service('/Users/patty/Chrome_driver/chromedriver')
driver = webdriver.Chrome(options=options,service=s)
driver.set_page_load_timeout(10)
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html5lib')
print(soup.find('h2').text)
driver.implicitly_wait(10)

driver.find_element_by_xpath('//*[@id="nav"]/div/div[1]/ul[1]/li[1]/a/span').click()

driver.quit()
  