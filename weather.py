import requests

article_id = ['Лондон', 'Шереметьево', 'Череповец']

for i in article_id:
    try:
        url_template = 'https://wttr.in/{}?n?M?q?T&lang=ru'
        url = url_template.format(i)
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)
    except:
        print(f'Информация о погоде в городе {i} временно недоступен\n')