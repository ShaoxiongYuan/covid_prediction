import requests
import warnings

warnings.filterwarnings('ignore')


def province_covid_num(prov):
    pass


def province_population(prov):
    pass


def predict(population, infected, exposed, removed, quarantine_num, lurk_num):
    pass

# 疫情数据
# content = requests.get(
#     'https://master-covid-19-api-laeyoung.endpoint.ainize.ai/jhu-edu/timeseries?iso2=CN').json()
#
# for item in content:
#     print(item['provincestate'])
#
#
#
# # 人口数据
# # 用来定义头部
# headers = {}
# # 用来传递参数
# keyvalue = {}
# # 目标网址
# url = 'http://data.stats.gov.cn/easyquery.htm'
# # 头部填充
# headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' \
#                         'AppleWebKit/537.36 (KHTML, like Gecko)' \
#                         'Chrome/70.0.3538.102 Safari/537.36'
#
# # 参数填充
# keyvalue['m'] = 'QueryData'
# keyvalue['dbcode'] = 'fsnd'
# keyvalue['rowcode'] = 'zb'
# keyvalue['colcode'] = 'sj'
# keyvalue['wds'] = '[]'
# keyvalue['dfwds'] = '[{"wdcode":"zb","valuecode":"A0301"}, ' \
#                     '{valuecode: "110000", wdcode: "reg"}, ' \
#                     '{valuecode: "2020", wdcode: "sj"}]'
#
# response = requests.get(url, headers=headers, params=keyvalue, verify=False)
# data = response.json()
# pop_2020 = data['returndata']['datanodes'][0]['data']['data']
# print(pop_2020)
