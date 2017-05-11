from bs4 import BeautifulSoup
import requests
import re
import json

url = 'http://www.passportapproved.com/playlist.php'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

s = soup.select('td')

for item in s:
    r = re.findall('(.+) - "(.+)"', item.text.strip())
    if(r != []):
        break
song_dict = {}
for pair in r:
    song_dict[pair[0]] = pair[1]

with open('./songs.json', 'w') as f:
    json.dump(song_dict, f)
