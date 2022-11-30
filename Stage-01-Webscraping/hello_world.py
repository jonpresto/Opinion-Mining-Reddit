print('howdy')
# ref link https://www.youtube.com/watch?v=FdjVoOf9HN4&t=159s

import sys
import subprocess

# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pandas'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'numpy'])

import requests
import pandas as pd
import numpy as np


CLIENT_ID = 'wHg_1bNEVbRHEN7ajiC5Tw'
SECRET_KEY = 'Z5bY7PWrsxUS3CykE9BYQYtu05HPEA'
auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)

with open('pw.txt', 'r') as f:
    pw = f.read()

data = {
    'grant_type': 'password',
    'username': 'PrincipleEmergency62',
    'password': pw
}

headers = {'User-Agent': 'MyAPI/0.0.1'}
res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)
TOKEN = res.json()['access_token']
headers['Authorization'] = f'bearer {TOKEN}'

#demo1
#out = requests.get('https://oauth.reddit.com/api/v1/me', headers=headers).json()
#print(out)

#demo2
res = requests.get('https://oauth.reddit.com/r/python/hot',
                   headers = headers,
                   params={'limit': '100'})

#print(res.json())
#for post in res.json()['data']['children']:
#    print(post['data']['title'])



df = pd.DataFrame()

for post in res.json()['data']['children']:
    df = df.append({
        'subreddit': post['data']['subreddit'],
        'title': post['data']['title'],
        'selftext': post['data']['selftext'],
        'upvote_ratio': post['data']['upvote_ratio'],
        'ups': post['data']['ups'],
        'downs': post['data']['downs'],
        'score': post['data']['score']

    }, ignore_index=True)

print(df)

print(post['data'].keys())