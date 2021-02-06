from lxml import html
from bs4 import BeautifulSoup
from urllib.request import urlopen

def get_price(code):
    base_url = 'https://kabutan.jp/stock/?code='
    try:
        target = base_url+str(code)
        html = urlopen(target)
        soup = BeautifulSoup(html, 'html.parser')
        #priceに株価,changeに変動した円,percent_changeに変動率を入れる。
        price = soup.select_one('#stockinfo_i1 > div.si_i1_2 > span.kabuka').text
        change = soup.select_one('#stockinfo_i1 > div.si_i1_2 > dl > dd:nth-child(2) > span').text + '円'
        percent_change = soup.select_one('#stockinfo_i1 > div.si_i1_2 > dl > dd:nth-child(3) > span').text + '%'
        return [price, change, percent_change]
    except Exception as e:
        return str(code) + ':' + str(e)

if __name__ == "__main__":
    get_price()