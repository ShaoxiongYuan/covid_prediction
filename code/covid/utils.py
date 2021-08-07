import requests
import warnings

warnings.filterwarnings('ignore')

id_map = {'Beijing': '110000', 'Tianjin': '120000'}


def province_covid_num(prov):
    pass


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
    print(pop_2020)


# 疫情数据
# content = requests.get(
#     'https://master-covid-19-api-laeyoung.endpoint.ainize.ai/jhu-edu/timeseries?iso2=CN').json()
#
# for item in content:
#     print(item['provincestate'])
#
#
#

province_population('Beijing')
