import requests
from bs4 import BeautifulSoup
import math     #切り上げ用

card_name = input("カード名を入力してください")   #検索したいカード名を入力

#カードラボ検索
rabo_url = 'https://www.c-labo-online.jp/product-list?keyword={}'.format(card_name) #getメソッドを利用して、カード検索後のURLを作成

rabo_html = requests.get(rabo_url)
rabo_soup = BeautifulSoup(rabo_html.content, 'html.parser')

try:
    item_count_str = rabo_soup.find('span', class_ = 'number')  #商品の総件数を取得（ページをまたいだスクレイピングに使う）
    item_count = int(item_count_str.text.replace(',', ''))      #商品の総件数を整数化する
    pages = math.ceil(item_count / 60)      #総ページ数を算出(カードラボでは1ページに最大60アイテム表示される)
    
    for view in range(1, pages + 1):        #総ページぶん繰り返す
        page_url = rabo_url + '&page=' + str(view)  #getメソッドを利用してページナンバーを指定したURLを作成

        now_page = requests.get(page_url)                                       #現在のページを取得
        now_page_soup = BeautifulSoup(now_page.content, 'html.parser')          #現在のページをパース
        item_data = now_page_soup.find_all('div', class_ = 'list_item_data')    #現在のページのitem_dataクラスを全て抽出

        print('--------------------' + str(view) + 'ページ目--------------------')        #ページ番号を表示

        for item in item_data:                                              #現在のページのitem_data数ぶん繰り返す
            item_name = item.find('span', class_ = 'goods_name')            #商品名を取得
            item_price = item.find('span', class_ = 'figure')               #価格を取得
            print(item_name.text, item_price.text)                          #商品名と価格を表示

except Exception as e:              #一応エラー処理
    print('エラーが発生しました')   
    print(type(e))
    print(e)
    pass