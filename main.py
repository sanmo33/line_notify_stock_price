from modules.base import get_price

import requests
import configparser

#config.iniからlineのkeyを持ってくる。
config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='UTF-8')
line_key = config_ini['API']['Key']

#line notifyの設定をする
TOKEN = line_key
api_url = 'https://notify-api.line.me/api/notify'
TOKEN_dic = {'Authorization': 'Bearer' + ' ' + TOKEN}

base_url = 'https://kabutan.jp/stock/?code='
#keyに企業名、valueに証券コードを入れる
codes_dic = {
    '任天堂':7974
}

price_dic = {}

for key ,value in codes_dic.items():
    price_dic[key] = get_price(value)

for key , value in price_dic.items():
    send_dic = {}
    temp_str = ' '.join(value)
    send_dic['message'] = key + ' ' + temp_str
    requests.post(api_url, headers=TOKEN_dic, data = send_dic)
