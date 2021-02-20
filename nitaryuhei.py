##########################################################################
#新田竜平と見せかけての、IT用語をgoogleで検索して、一番上にヒットしたURLを拾ってくる       #
##########################################################################

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
SERVICE_ACCOUNT_FILE = '/Users/iwasawayuusaku/Documents/googleのキー/秘密だお❤︎'  #秘密鍵のjsonファイル
#ServiceAccountCredentialsのfrom_json_keyfile_name関数を使って認証情報を作成
#1つ目の引数＝秘密鍵のPATH 二つ目＝APIの情報
credentials = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_FILE,SCOPES)
#認証情報をgspreadのauthorize関数に渡してスプレッドシートの操作権を取得
gs = gspread.authorize(credentials)
#スプレッドシートのURLのd/と/editの間の文字列がスプレッドシートキー.
SPREDSHEET_KEY = 'おっとっと公開しませんよ'
#スプシのキーとシート名をopen_by_key関数に渡すことでシート情報を取得
workbook = gs.open_by_key(SPREDSHEET_KEY)
worksheet = workbook.worksheet("用語集")         #どのシートを開くのか、直接シート名で指定

#google様のurl
url = 'https://www.google.co.jp/search'
#google検索をする準備　Webdriverでクロームを立ち上げ

##########################################################################
#google検索をして、一番上のHitしたurlを拾ってくる関数(url_get)                     # 
##########################################################################
def url_get(driver):
    loop = 1             #loopした回数を記録するもの
    max_loop = 1         #最大のループ回数今回は1
    #タイトルとリンクはclass="r"に入っているらしい？だめなら→gでやる
    class_group = driver.find_elements_by_class_name('g')
    #そのうちのリンクを1番上だけ取得してみる
    for elem in class_group:
        tophit_url = elem.find_element_by_tag_name('a').get_attribute('href')
        if loop == max_loop :
            break
        else:
            loop += 1
    return tophit_url
##########################################################################

#セルの値を取得するには、acell関数もしくはcell関数を用いる
IDX1 = 1        #ループした回数を管理
in_row = 2      #入力の列の番号  2行目が用語※固定
out_row = 7     #出力の列の番号　7行目に出力※固定
cols_num = 4    #単語が入力されている行（4行目から）※インクリしてどんどん下へ降る
max_IDX = 2     #最大のループ回数

#単語を取得して、スクレイピング
while IDX1 <= max_IDX:
    word = worksheet.cell(cols_num, in_row).value  #２列目の単語をword変数に代入
    if word == "":   #単語未入力で終了
        break
    driver = webdriver.Chrome()
    driver.get('https://www.google.com/')  #一旦は何回もgoogle開いちゃうくそ雑魚コードでできるかお試し。今後改善
    search = driver.find_element_by_name('q')
    search.send_keys(word)
    search.submit()
    time.sleep(1)         #時間を遅らせないと、googleが攻撃されたと思うらしい.怖い世の中
    #今のままだと、単語がどんどん連結されて検索してしまう。一旦はgoogleを何度も開かせてやってみる改善する！！！！
    return_url = url_get(driver)　　　　　　　 #urlゲットの関数を使用して、変数に代入
    #なんの単語検索して、どんなurlを取得下のか一応みたい.めんどいから一旦これで確認
    print(word)
    print(return_url)
    #取得したurlをスプシに書き出す
    worksheet.update_cell(cols_num, out_row, return_url)
    cols_num += 1          #行番号をインクリメント
    IDX1 += 1              #ループ回数をインクリメント


"""
#新規でシートを作成するには、add.worksheet(title="シート名",rows=列数, cols=行数)
#書き出すには　　set_with_dataframe(書き出すシート名,)
できなあああああい。多分、dataframe関数が、dataとか表に特化しているものだと考えた→正解pandasのやつ
書き出すには　　update_acell  もしくは　update_cell
"""