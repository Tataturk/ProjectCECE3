#%%
import requests
url = "https://www.projectcece.nl/api/hva/catalog/product/?format=json"
headers = {"Authorization": "Token 3d1538bc7eae631f88d68299602b3ac60205ffe4",
            'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5)'
                          'AppleWebKit/537.36 (KHTML, like Gecko)'
                          'Chrome/45.0.2454.101 Safari/537.36'),
                          'referer': 'http://stats.nba.com/scores/'}
r = requests.get(url, headers=headers)
content = r.json()
data = content['results']
#print(content)
#%%
while content['next'] is not 'None':
    
    url = content['next']
    print("Requesting information from", url)
    r = requests.get(url,headers=headers)
    print("Received!")
    content = r.json()

    data.extend(content['results'])
#%%
print(data)
