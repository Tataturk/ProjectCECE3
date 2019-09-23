import requests
import pandas as pd
url = "https://www.projectcece.nl/api/hva/analytics/?date=20190922"
headers = {"Authorization": "Token 3d1538bc7eae631f88d68299602b3ac60205ffe4",
            'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5)'
                          'AppleWebKit/537.36 (KHTML, like Gecko)'
                          'Chrome/45.0.2454.101 Safari/537.36'),
                          'referer': 'http://stats.nba.com/scores/'}
r = requests.get(url, headers=headers)
content = r.json()

df = pd.DataFrame(content)

df.head()