import requests
import json

content = requests.get(
    'https://master-covid-19-api-laeyoung.endpoint.ainize.ai/jhu-edu/timeseries?iso2=CN').content.decode()

content = json.loads(content)
for item in content:
    print(item['provincestate'])