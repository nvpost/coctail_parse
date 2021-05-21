# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

import coctail_item_parse as cip

url = "https://ru.inshaker.com/cocktails?random_page=2"
page = requests.get(url)


soup = BeautifulSoup(page.text, "html.parser")

coctails = soup.findAll(class_='cocktail-item')

start_url = "https://ru.inshaker.com"

en_title=''
for coctail in coctails:
    id = coctail['data-id']
    title = coctail.find(class_='cocktail-item-name').text.replace('\xa0', ' ')
    img_src = coctail.find(class_='cocktail-item-image')['src']
    coctail_url = coctail.find(class_='cocktail-item-preview')['href']
    coctail_item_data = cip.parse(start_url+coctail_url)

    row={'id':id, 'title':title}

    # print(row)
    # print(coctail_item_data)
