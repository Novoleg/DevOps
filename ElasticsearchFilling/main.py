import requests
res = requests.get('http://192.168.100.7:9200')
print(res.content)