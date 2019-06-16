ls
import os, re, requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

with open('meigen.txt', 'a') as f:
    for i in range(1, 16):
        url = 'http://iyashitour.com/meigen/theme/life/{}'.format(i)
        html = urlopen(url)
        data = html.read()
        html = data.decode('utf-8')

        soup = BeautifulSoup(html, 'html.parser')
        # ダウンロードしたデータを表示
        print(soup)

        p_elem = soup.find_all('p')
        meigens_row = ""
        flg = False
        for meigen in p_elem:
            meigen = str(meigen)
            if meigen == "<p> </p>" and flg == False:
                flg = True
                continue
            elif meigen == "<p> </p>" and flg == True:
                flg = False
            if flg == True:
                meigens_row += meigen + '\n'

        # bタグの排除
        meigens = re.sub(r'<(/)?\w+>?', '', meigens_row)
        #「」の排除
        meigens = re.sub(r'(「|」)', '', meigens)
        # 例外の開始文字から始まる文字列を排除
        meigens = re.sub(r'((\(|【|-|※|\s/)(\d|\D)+)?', '', meigens)
        # 改行の排除
        meigens = re.sub(r'\n', '', meigens)

        # 生成データの確認
        print(meigens)

        # f.write(meigens)