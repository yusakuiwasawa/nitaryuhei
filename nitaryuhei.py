"""
新田竜平と見せかけての、IT用語をgoogleで検索して、一番上にヒットしたURLを拾ってくる
"""
#まずはimport
import time
import requests
from selenium import webdriver
import chromedriver_binary 
from bs4 import BeautifulSoup

#google様のurl
url = 'https://www.google.co.jp/search'

"""
#指定の単語でgoogole検索。
word = "岩澤優作"
response = requests.get(url, params={'q':word, 'num':2})
print(response.url)

top_hit = requests.get(response.url)
top_hit = BeautifulSoup(top_hit.text, "html.parser")
serch_result = top_hit.select('.r > a')
print(serch_result)
"""

word = "岩澤優作"
#google検索をする準備
driver = webdriver.Chrome()
driver.get('https://www.google.com/')
search = driver.find_element_by_name('q')
search.send_keys(word)
search.submit()
time.sleep(1)