from bs4 import BeautifulSoup
import requests

def parse(coctail_url):

    page = requests.get(coctail_url)
    soup = BeautifulSoup(page.text, "html.parser")

    en_title = soup.find(class_='name-en').text.replace('\xa0', ' ')
    tags_list = soup.find(class_='tags').findAll(class_='tag')
    tags = get_tags(tags_list)

    ingredients = soup.find(class_='ingredient-tables').findAll('table')[0]
    tools = soup.find(class_='ingredient-tables').findAll('table')[0]
    get_ingrediens(ingredients)
    get_tools(tools)

    process_arr = soup.find(class_='steps').findAll('li')
    process = "; ".join(list(map(lambda x: x.text.replace('\xa0', ' '), process_arr)))

    text_info=''
    try:
        text_info = soup.find(id='cocktail-tag-text').find('p').text.replace('\xa0', ' ')
    except:
        text_info = ''
    # if soup.find(id='cocktail-tag-text').find('p'):
    #     text_info = soup.find(id='cocktail-tag-text').find('p').text.replace('\xa0', ' ')

    print(text_info)

    return {'en_title':en_title, 'process':process, 'text_info':text_info}


def get_tags(tags_list):
    tags = []
    for tag in tags_list:
        tags.append(tag.text)
    # сохранить в отдельную базу с id коктейля
    return tags

def get_imgs(img_list):
    imgs = []

def get_ingrediens(ingredients):
    name = ingredients.find(class_='name').text
    amount = ingredients.find(class_='amount').text
    unit = ingredients.find(class_='unit').text
    row = {'name':name, 'amount':amount, 'unit':unit}

    #сохранить в отдельную базу с id коктейля

def get_tools(tools):
    name = tools.find(class_='name').text
    amount = tools.find(class_='amount').text
    unit = tools.find(class_='unit').text
    row = {'name':name, 'amount':amount, 'unit':unit}

    #сохранить в отдельную базу с id коктейля