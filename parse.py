# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

import coctail_item_parse as cip
import sql as sql

url = "https://ru.inshaker.com/cocktails?random_page=2"
page = requests.get(url)


soup = BeautifulSoup(page.text, "html.parser")

coctails = soup.findAll(class_='cocktail-item')

start_url = "https://ru.inshaker.com"

en_title=''
for coctail in coctails:
    id = int(coctail['data-id'])
    name = coctail.find(class_='cocktail-item-name').text.replace('\xa0', ' ')
    img_src = coctail.find(class_='cocktail-item-image')['src']
    coctail_url = coctail.find(class_='cocktail-item-preview')['href']
    coctail_item_data = cip.parse(id, start_url+coctail_url)

    main_row={'id':id, 'name':name}
    row = {**main_row, **coctail_item_data}


    query = "INSERT INTO coctails(coctail_id, name, en_name, process, text_info) VALUES(%s, %s, %s, %s, %s)"


    args = (row['id'], row['name'], row['en_name'], row['process'], row['text_info'])

    # try:
    #     sql.cursor.execute(query, args)
    #     sql.conn.commit()
    #     print(args)
    # except:
    #     print('ошибка')



    # print(coctail_item_data)
