import os
import secrets
import requests
from PIL import Image

from covid import app
from .variables import id_map, translation_map


def province_covid_num(prov):
    url = 'https://master-covid-19-api-laeyoung.endpoint.ainize.ai/jhu-edu/timeseries?iso2=CN'
    content = requests.get(url).json()

    for item in content:
        if item['provincestate'] == prov:
            confirmed = item['timeseries']['8/4/21']['confirmed']
            deaths = item['timeseries']['8/4/21']['deaths']
            recovered = item['timeseries']['8/4/21']['recovered']
            return confirmed - deaths - recovered, recovered


def province_population(prov):
    headers = {}
    # 用来传递参数
    keyvalue = {}
    # 目标网址
    url = 'http://data.stats.gov.cn/easyquery.htm'
    # 头部填充
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' \
                            'AppleWebKit/537.36 (KHTML, like Gecko)' \
                            'Chrome/70.0.3538.102 Safari/537.36'

    # 参数填充
    keyvalue['m'] = 'QueryData'
    keyvalue['dbcode'] = 'fsnd'
    keyvalue['rowcode'] = 'zb'
    keyvalue['colcode'] = 'sj'
    keyvalue['wds'] = '[]'
    id = id_map[prov]
    keyvalue['dfwds'] = '[{"wdcode":"zb","valuecode":"A0301"}, ' \
                        '{valuecode: ' + id + ', wdcode: "reg"}, ' \
                                              '{valuecode: "2020", wdcode: "sj"}]'

    response = requests.get(url, headers=headers, params=keyvalue, verify=False)
    data = response.json()
    pop_2020 = data['returndata']['datanodes'][0]['data']['data']
    return pop_2020


risk_map = {}


def get_risk_map():
    url = 'https://file1.dxycdn.com/2021/0202/196/1680100273140422643-135.json'
    content = requests.get(url).json()
    for area in content['data'][1]['dangerPros']:
        name = area['provinceShortName']
        risk_map[translation_map[name]] = 1

    for area in content['data'][0]['dangerPros']:
        name = area['provinceShortName']
        risk_map[translation_map[name]] = 2


def province_risk(prov):
    get_risk_map()
    if prov in risk_map.keys():
        return risk_map[prov]
    else:
        return 0


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn
