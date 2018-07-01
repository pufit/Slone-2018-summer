from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from os import path, mkdir

save_dir = 'downloaded'
url = 'http://c.xkcd.com/random/comic/'

try:
    mkdir(save_dir)
except OSError:
    pass

print('Downloading...')

req = urlopen(Request(url))
html = req.read()
img_id = req.url.split('/')[3]
dom = BeautifulSoup(html, "html.parser")
img = list(dom.find('div', id='comic').children)[1]


try:
    mkdir(path.join(save_dir, img_id))
except OSError:
    pass


with open(path.join(save_dir, img_id, img_id + '.jpg'), 'wb') as f:
    f.write(urlopen(Request('http:' + img['src'])).read())

with open(path.join(save_dir, img_id, img_id + '.txt'), 'w', encoding='utf-8') as f:
    f.write(img['title'])

print('Done: ' + str(img_id))
