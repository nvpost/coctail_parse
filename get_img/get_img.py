import pymysql
import requests


conn = pymysql.connect(host='localhost',
                       user='root',
                       password='mysql',
                       db='coctails_base',
                       charset='utf8mb4')

cursor = conn.cursor(pymysql.cursors.DictCursor)

select_img_query = "SELECT src FROM coctails"

cursor.execute(select_img_query)

imgs = cursor.fetchall()

main_url = "https://ru.inshaker.com"
for img in imgs:
    src = main_url+img['src']
    filename = img['src'].split('/')[-1]
    print(src)

    r = requests.get(src, allow_redirects=True)
    file = open('imgs/'+filename, 'wb')
    file.write(r.content)
    print(file)
    file.close()
