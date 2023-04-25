import requests

cities = ['Лондон', 'Шереметьево', 'Череповец']
for city in cities:
    try:
        url_template = 'https://wttr.in/{}?n?M?q?T&lang=ru'
        url = url_template.format(city)
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)
    except:
        print(f'Информация о погоде в городе {city} временно недоступен\n')