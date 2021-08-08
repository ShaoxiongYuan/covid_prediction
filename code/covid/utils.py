import requests
import warnings

warnings.filterwarnings('ignore')

id_map = {'Beijing': '110000', 'Tianjin': '120000', 'Hebei': '130000',
          'Shanxi': '140000', 'Inner Mongolia': '150000', 'Liaoning': '210000',
          'Jilin': '220000', 'Heilongjiang': '230000', 'Shanghai': '310000',
          'Jiangsu': '320000', 'Zhejiang': '330000', 'Anhui': '340000',
          'Fujian': '350000', 'Jiangxi': '360000', 'Shandong': '370000',
          'Henan': '410000', 'Hubei': '420000', 'Hunan': '430000',
          'Guangdong': '440000', 'Guangxi': '450000', 'Hainan': '460000',
          'Chongqing': '500000', 'Sichuan': '510000', 'Guizhou': '520000',
          'Yunnan': '530000', 'Tibet': '540000', 'Shaanxi': '610000',
          'Gansu': '620000', 'Qinghai': '630000', 'Ningxia': '640000',
          'Xinjiang': '650000'}

risk_map = {}

translation_map = {'北京': 'Beijing', '天津': 'Tianjin', '上海': 'Shanghai',
                   '重庆': 'Chongqing', '河北': 'Hebei', '山西': 'Shanxi',
                   '辽宁': 'Liaoning', '吉林': 'Jilin', '黑龙江': 'Heilongjiang',
                   '江苏': 'Jiangsu', '浙江': 'Zhejiang', '安徽': 'Anhui',
                   '福建': 'Fujian', '江西': 'Jiangxi', '山东': 'Shandong',
                   '湖北': 'Hubei', '湖南': 'Hunan', '广东': 'Guangdong',
                   '海南': 'Hainan', '四川': 'Sichuan', '贵州': 'Guizhou',
                   '云南': 'Yunnan', '陕西': 'Shaanxi', '甘肃': 'Gansu',
                   '青海': 'Qinghai', '内蒙古': 'Inner Mongolia', '西藏': 'Tibet',
                   '广西': 'Guangxi', '宁夏': 'Ningxia', '新疆': 'Xinjiang',
                   '河南': 'Henan'}


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
    if prov in risk_map.keys():
        return risk_map[prov]
    else:
        return 0
