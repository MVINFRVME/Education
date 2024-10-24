# Задача 2. Документация API
# Обычно к открытым API прилагается подробная документация, где описывается логика формирования ссылок и
# какие данные по ним можно получать (или отправлять!).
# Изучите документацию того же сайта по «Звёздным войнам».
# Поэкспериментируйте с получением данных о кораблях, планетах, фильмах и так далее.


import requests
import json

result = requests.get('https://swapi.dev/api/films/4/')
data = json.loads(result.text)
print(data['opening_crawl'])