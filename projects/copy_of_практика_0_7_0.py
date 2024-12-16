# -*- coding: utf-8 -*-
"""Copy of Практика 0.7.0

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19oZgOID6XKMDfiGSNwiLgl3hASoRO5Rv

ФИО:
"""



"""## Задание 1. HTTP-запросы, ответы и погода

Напишите HTTP-запрос для получения информации о погоде в введенном городе из API. Можно использовать API: https://open-meteo.com/. Используйте метод GET.


Ввод
```
56.50, 60.35
```

Вывод
```
Сегодня (1.11) погода 20 ◦С, нет осадков, туман
```




"""

import requests
from datetime import datetime
city = input("")
url = f"https://api.gismeteo.net/v2/weather/current/?city={city}"
headers = {
    'X-Gismeteo-Token': 'YOUR_API_KEY'
    }
response = requests.get(url, headers=headers)
if response.status_code == 200:
    data = response.json()
    temp = data['response']['temperature']['air']['C']
    precip = data['response']['precipitation']['type']
    phenomenon = data['response']['phenomenon']['type']
    precip_text = "без осадков" if precip == "none" else precip
    phenomenon_text = "ясно" if phenomenon == "clear" else phenomenon
    date = datetime.now().strftime("%d.%m")
    print(f"Сегодня ({date}) в {city} {temp} градусов тепла, {precip_text}, {phenomenon_text}.")
else:
    print("Не удалось получить данные о погоде.")

"""## Задание 2. HTTP-запросы, ответы и покемоны


Создайте код программы, которая будет взаимодействовать с API, со следующим функионалом:

1. Используя метод GET, отправьте запрос на endpoint /pokemon, чтобы получить список первых 20 покемонов

2. Извлеките имена покемонов из ответа и выведите их списком

3. Введите с помощью input() название одного из покемонов


```
Имя покемона: clefairy
```



4. Отправьте GET-запрос, чтобы получить полную информацию о выбранном покемоне

5. Извлеките и выведите следующие данные о введенном покемоне:

     • Имя

     • Тип

     • Вес

     • Рост

     • Способности

Используйте PokéAPI (https://pokeapi.co/), который предоставляет информацию о покемонах, их характеристиках, типах и другую информацию.
"""

import requests

url = "https://pokeapi.co/api/v2/pokemon?limit=20"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()

    pokemon_names = [pokemon['name'] for pokemon in data['results']]
    print("Список первых 20 покемонов:")
    for name in pokemon_names:
        print(name)
else:
    print("Не удалось получить список покемонов")
    exit()


selected_pokemon = input("\nВведите название одного из покемонов из списка: ").strip().lower()
url = f"https://pokeapi.co/api/v2/pokemon/{selected_pokemon}"
response = requests.get(url)


if response.status_code == 200:
    pokemon_data = response.json()
    name = pokemon_data['name']
    types = [t['type']['name'] for t in pokemon_data['types']]
    weight = pokemon_data['weight']
    height = pokemon_data['height']
    abilities = [ability['ability']['name'] for ability in pokemon_data['abilities']]

    print(f"\nИмя: {name}")
    print(f"Тип: {', '.join(types)}")
    print(f"Вес: {weight / 10} кг")
    print(f"Рост: {height / 10} м")
    print(f"Способности: {', '.join(abilities)}")
else:
    print("Не удалось получить информацию о выбранном покемоне")

"""## Задание 3. HTTP-запросы, ответы и посты

Создайте программу, которая будет взаимодействовать с JSONPlaceholder API, реализуя следующие функции:

1. Реализуйте функцию, которая выполняет GET-запрос к https://jsonplaceholder.typicode.com/posts и возвращает список постов в формате JSON

2. Реализуйте функцию, котороая получает вводимое ID поста, выполняет GET-запрос по ID и возвращает данные поста в формате JSON

3. Реализуйте функцию, которая выполняет обработку JSON из пункта 2 и выводит всю важную информацию в консоль
"""

import requests

url_all_posts = "https://jsonplaceholder.typicode.com/posts"
response_all_posts = requests.get(url_all_posts)

if response_all_posts.status_code == 200:
    posts = response_all_posts.json()
    print(f"Получено {len(posts)} постов.")
else:
    print("Не удалось получить список постов.")
    posts = []
post_id = input("Введите ID поста для получения подробной информации: ")
url_post_by_id = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
response_post_by_id = requests.get(url_post_by_id)
if response_post_by_id.status_code == 200:
    post_data = response_post_by_id.json()
else:
    print(f"Не удалось получить пост с ID {post_id}.")
    post_data = {}

if post_data:
    print("\nИнформация о посте:")
    print(f"ID: {post_data.get('id')}")
    print(f"User ID: {post_data.get('userId')}")
    print(f"Title: {post_data.get('title')}")
    print(f"Body: {post_data.get('body')}")
else:
    print("Данные поста отсутствуют.")

"""## Задание 4. HTTP-запросы, ответы и работа с постами

Создайте программу, которая будет взаимодействовать с JSONPlaceholder API (из предыдущего задания), реализуя новые функции:

1. Реализуйте функцию, которая принимает заголовок, содержимое и ID пользователя (информация вводится с помощью input()), выполняет POST-запрос для создания нового поста и возвращает информацию о созданном посте в формате JSON


```
Заголовок: Новый пост
Содержимое поста: Тут должно находиться содержимое нового поста...
ID пользователя: 10
```



2. Реализуйте функцию, которая принимает ID поста, новый заголовок и новое содержимое, выполняет PUT-запрос и возвращает обновлённый пост в формате JSON

3. Реализуйте функцию, которая принимает ID поста, выполняет DELETE-запрос и возвращает статус-код ответа
"""



"""## Задание 5. HTTP-запросы, ответы и пёсики

Создайте программу, которая будет взаимодействовать с Dog API, которая позволит получать список пород собак, вводить несколько пород и получать их фотогрфии.

Этапы:

1. Создайте функцию, которая использует метод GET и возвращает список всех пород собак в формате нумерованного списка

2. Реализуйте возможность ввода нескольких пород собак через запятую


```
african, chow, dingo
```



3. Создание функции, которая реализует запрос, возвращает и выводит изображениия собак, породы которых были введены до этого


Используйте Dog API (https://dog.ceo/dog-api/), который предоставляет информацию о породах собак и их изображения.

"""

import requests
from IPython.display import Image, display

url = "https://dog.ceo/api/breeds/list/all"
response = requests.get(url)

if response.status_code == 200:
    breeds = response.json()['message']
    breed_list = [f"{index + 1}. {breed}" for index, breed in enumerate(breeds.keys())]
    print("Список всех пород собак:")
    print("\n".join(breed_list[:20]))
else:
    print("Не удалось получить список пород собак.")
    breeds = {}

user_input = input("Введите названия пород через запятую (african, chow, dingo): ")
selected_breeds = [breed.strip().lower() for breed in user_input.split(",")]


images = {}
for breed in selected_breeds:
    url = f"https://dog.ceo/api/breed/{breed}/images/random"
    response = requests.get(url)

    if response.status_code == 200:
        images[breed] = response.json()['message']
    else:
        images[breed] = "Не удалось получить изображение для этой породы."

print("\nИзображения выбранных пород:")
for breed, image_url in images.items():
    print(f"{breed.capitalize()}: {image_url}")
    if "http" in image_url:
        display(Image(url=image_url))