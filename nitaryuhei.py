"""
新田竜平と見せかけての、IT用語をgoogleで検索して、一番上にヒットしたURLを拾ってくる
"""
#まずはimport
import time
import requests
from selenium import webdriver
import chromedriver_binary 
from bs4 import BeautifulSoup
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from gspread_dataframe import set_with_dataframe

#jsonファイルを使って、認証情報を取得 scopesってみんな同じなん？
SCOPES =  ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = '/Users/iwasawayuusaku/Documents/googleのキー/公開はしませんよ笑'  #秘密鍵のjsonファイル
#ServiceAccountCredentialsのfrom_json_keyfile_name関数を使って認証情報を作成
#1つ目の引数＝秘密鍵のPATH 二つ目＝APIの情報
credentials = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_FILE,SCOPES)
#証情報をgspreadのauthorize関数に渡してスプレッドシートの操作権を取得
gs = gspread.authorize(credentials)
#スプレッドシートのURLのd/と/editの間の文字列がスプレッドシートキー.
SPREDSHEET_KEY = 'おっとっと、こちらも公開しませんよ❤︎'
#スプシのキーとシート名をopen_by_key関数に渡すことでシート情報を取得
workbook = gs.open_by_key(SPREDSHEET_KEY)
worksheet = workbook.worksheet("用語集")
"""
#セルの値を取得するには、acell関数を用いる
IDX1 = 4        #用語の列をぶん回すためのインデックス
max_IDX = 6    #最大のインデックス
while IDX1 <= max_IDX:
    if worksheet.acell("B" + str(IDX1)).value == "":   #単語未入力で終了
        break
    #print(worksheet.acell("B" + str(IDX1)).value)
    
    IDX1 += 1
"""
#新規でシートを作成するには、add.worksheet(title="シート名",rows=列数, cols=行数)
#書き出すには　　set_with_dataframe(書き出すシート名,)
"""できなあああああい。多分、dataframe関数が、dataとか表に特化しているものだと考えた"""
set_with_dataframe(workbook.worksheet("用語集"), "a")

"""
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
time.sleep(1)         #時間を遅らせないと、googleが攻撃されたと思うらしい

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
"""