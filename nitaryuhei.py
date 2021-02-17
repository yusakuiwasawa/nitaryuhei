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

#検索したいwordを入れる
word = "岩澤優作"
#google検索をする準備
driver = webdriver.Chrome()
driver.get('https://www.google.com/')
search = driver.find_element_by_name('q')
search.send_keys(word)
search.submit()
time.sleep(1)

#google検索をして、一番上のHitしたurlを拾ってくる関数
def url_get(driver):
    tophit_url = []      #とりあえず、Hitしたurlの格納先を作っておく
    loop = 1             #loopした回数を記録するもの
    max_loop = 1         #最大のループ回数今回は1
    #タイトルとリンクはclass="r"に入っているらしい？だめなら→gでやる
    class_group = driver.find_elements_by_class_name('g')
    #そのうちのリンクを1番上だけ取得してみる
    for elem in class_group:
        tophit_url.append(elem.find_element_by_tag_name('a').get_attribute('href'))
        if loop == max_loop :
            break
        else:
            loop += 1
    return tophit_url

print(url_get(driver))