from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from os import path

save_dir = 'downloaded'
url = 'http://c.xkcd.com/random/comic/'

print('Downloading...')

req = urlopen(Request(url))
html = req.read()
img_id = req.url.split('/')[3]
doc_structure = BeautifulSoup(html, "html.parser")
img = BeautifulSoup(html, "html.parser").findAll('img')[1]


with open(path.join(save_dir, img_id + '.jpg'), 'wb') as f:
    f.write(urlopen(Request('http:' + img['src'])).read())

with open(path.join(save_dir, img_id + '.txt'), 'w', encoding='utf-8') as f:
    f.write(img['title'])

print('Done: ' + str(img_id))
