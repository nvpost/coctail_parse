from bs4 import BeautifulSoup
import requests

import sql

def parse(id, coctail_url):

    page = requests.get(coctail_url)
    soup = BeautifulSoup(page.text, "html.parser")

    en_name = soup.find(class_='name-en').text.replace('\xa0', ' ')
    tags_list = soup.find(class_='tags').findAll(class_='tag')
    tags = get_tags(id, tags_list)

    ingredients = soup.find(class_='ingredient-tables').findAll('table')[0]
    tools = soup.find(class_='ingredient-tables').findAll('table')[1]
    get_ingrediens(id, ingredients)
    get_tools(id, tools)

    process_arr = soup.find(class_='steps').findAll('li')
    process = "; ".join(list(map(lambda x: x.text.replace('\xa0', ' '), process_arr)))

    text_info=''
    try:
        text_info = soup.find(id='cocktail-tag-text').find('p').text.replace('\xa0', ' ')
    except:
        text_info = ''

    return {'en_name':en_name, 'process':process, 'text_info':text_info}


def get_tags(id, tags_list):
    tags = []
    for tag in tags_list:
        tags.append(tag.text)

        query = "INSERT INTO tags(coctail_id, tag) VALUES(%s, %s)"
        args = (id, tag.text)
        # addToSql(query, args)


    return tags

def get_imgs(img_list):
    imgs = []

def get_ingrediens(id, ingredients):
    for row in ingredients.findAll('tr'):
        try:
            name = row.find(class_='name').text
            amount = row.find(class_='amount').text
            unit = row.find(class_='unit').text

            query = "INSERT INTO ingredients(coctail_id, name, amount, unit) VALUES(%s, %s, %s, %s)"
            args = (id, name, amount, unit)
            # print(args)
            addToSql(query, args)
        except:
            print('заголовок')



def get_tools(id, tools):
    for row in tools.findAll('tr'):
        try:
            name = row.find(class_='name').text
            amount = row.find(class_='amount').text
            unit = row.find(class_='unit').text

            query = "INSERT INTO tools(coctail_id, name, amount, unit) VALUES(%s, %s, %s, %s)"
            args = (id, name, amount, unit)
            print(args)
            addToSql(query, args)
        except:
            print('заголовок')



def addToSql(query, args):
    try:
        sql.cursor.execute(query, args)
        sql.conn.commit()
        print(args)
    except:
        print('ошибка')