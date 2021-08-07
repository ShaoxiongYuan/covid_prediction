import requests
import warnings

warnings.filterwarnings('ignore')

# # 疫情数据
# content = requests.get(
#     'https://master-covid-19-api-laeyoung.endpoint.ainize.ai/jhu-edu/timeseries?iso2=CN').content.decode()
#
# content = json.loads(content)
# for item in content:
#     print(item['provincestate'])

# 人口数据
# for i in range(1, 6):
url = 'https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=fsnd&rowcode=zb&colcode=sj&wds=%5B%7B%22wdcode%22%3A%22reg%22%2C%22valuecode%22%3A%22110000%22%7D%5D&dfwds=%5B%5D'
response = requests.get(url, verify=False)
content = response.json()
print(content)
pop_2020 = content['returndata']['datanodes'][0]['data']['data']
print('2020 Population:', pop_2020)
