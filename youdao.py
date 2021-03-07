'''
i: cat
from: AUTO
to: AUTO
smartresult: dict
client: fanyideskweb
salt: 16151250958759 时间戳
sign: 5a917707cd8e91d89c0e5c8d3a56d1b9
lts: 1615125095875  时间戳同salt
bv: 818e2470a16ccb5d68270d01f2d298b2
doctype: json
version: 2.1
keyfrom: fanyi.web
action: FY_BY_REALTlME
'''
'''
i: dog
from: AUTO
to: AUTO
smartresult: dict
client: fanyideskweb
salt: 16151250524969
sign: a6bcd567a9c739e14a5bc97a347f13c6
lts: 1615125052496
bv: 818e2470a16ccb5d68270d01f2d298b2
doctype: json
version: 2.1
keyfrom: fanyi.web
action: FY_BY_REALTlME
'''

import time
import requests
import execjs
import hashlib
import random


t = execjs.eval('"" + (new Date).getTime()')
ran = str(execjs.eval('parseInt(10 * Math.random(), 10)'))
# t = str(int(time.time()*1000))
# ran = str(random.randint(0, 9))
word = input("输入需要翻译的单词：")
salt = t + ran
sign = hashlib.md5(("fanyideskweb" + word + salt + "Tbh5E8=q6U3EXe+&L[4c@").encode()).hexdigest()
bv = ''
lts = t
url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Length': '244',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'OUTFOX_SEARCH_USER_ID=-979823974@10.108.160.100; JSESSIONID=aaagNcgx9nFam-_kc9mGx; OUTFOX_SEARCH_USER_ID_NCOO=1135427900.757521; ___rl__test__cookies=1615126551898',
    'Host': 'fanyi.youdao.com',
    'Origin': 'http://fanyi.youdao.com',
    'Pragma': 'no-cache',
    'Referer': 'http://fanyi.youdao.com/',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}
params = {
    "i": word,
    "from": "AUTO",
    "to": 'AUTO',
    "smartresult": "dict",
    'client': 'fanyideskweb',
    'salt': salt,
    'sign': sign,
    'lts': lts,
    'bv': '818e2470a16ccb5d68270d01f2d298b2',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME'
}
# print(salt, sign, lts, end='++++')
res = requests.post(url=url, headers=headers, data=params)
print(res.text)