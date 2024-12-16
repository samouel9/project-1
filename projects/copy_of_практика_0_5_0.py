# -*- coding: utf-8 -*-
"""Copy of Практика 0.5.0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kuqhljW1CgLh__zOGD4UixGxUzqwW_G1

ФИО:
"""



"""# **Задание 1**

Дан словарь, содержащий имена и возраст людей, напишите программу выводящую возраст человека по имени

Дано:

```
{"Alice": 25, "Bob": 30, "Charlie": 35}
```

Вввод:


```
Alice
```

Вывод:


```
Alice 25
```
"""

people={"Alice": 25, "Bob": 30, "Charlie": 35}
neme=input('')
if neme in people:
  print(f'{neme} {people[neme]}')
else:
  print(f'{neme} Name not in list ):')

"""# **Задание 2**

Дан список, состоящий из целых чисел, необходимо написать функцию считающую сумму всех положительных четных чисел списка

Ввод:

```
1, 2, 3, 4, 5, 6, 7, 8, 9
```

Вывод:


```
20
```

***Запрещено:***

*   Использование готовых функций для суммирования чисел
"""

numbers =list(map(int, input('').split()))
result = 0
for num in numbers:
  if num > 0 and num % 2 == 0 :
    result += num
print(result)

"""# **Задание 3**

Дан словарь, содержащий название фрукта и его цвет, выведите список всех желтых фруктов


Дано:

```
fruits_and_flowers = {
    "apple": "rose",
    "banana": "lily",
    "mango": "sunflower",
    "orange": "daisy",
    "lemon": "tulip",
    "grape": "orchid"
}
```

Вывод:


```
Yellow fruits:
banana
lemon
mango
```
"""

fruits_and_flowers = {
    "apple": "rose",
    "banana": "lily",
    "mango": "sunflower",
    "orange": "daisy",
    "lemon": "tulip",
    "grape": "orchid"
}
yellow_fruits = ["banana", "mango", "lemon"]

print("Yellow fruits:")

for fruit in yellow_fruits:
    print(fruit)

"""# **Задание 4**

Дан словарь, необходимо написать функцию меняющую ключ и значение местами

Дано:


```
{"a": 1,"b": 2,"c": 3}
```

Вывод:

```
{1: 'a', 2: 'b', 3: 'c'}
```
"""

element = {"a": 1,"b": 2,"c": 3}
element1 = {s: a for s, a in element.items()}
print(element1 )

"""# **Задание 5**

Дан список слов, неограниченной длинны, сформируйте словарь, где в качестве ключа будет слово, а в качестве значения количество символов

**Критерии**


*   Словарь необходимо отсортировать по убыванию количества элементов в списке.
*   Подсчет элементов должен быть реализован в отдельной функции
*   Сортировка пары `ключ:значение` должна быть реализована также в виде отдельной функции




Дано:
```
['apple','banana','orange','apple','apple','banana']
```


Вывод:
```
{'apple':3, 'banana': 2, 'orange': 1}
```

***Запрещено:***

*   Использование готовых функций для сортировки словаря
*   Использование готовых функций для подсчета элементов
"""

words=['apple','banana','orange','apple','apple','banana']
num={}
for word in words:
  if word in num:
    num[word] += 1
  else:
    num[word] = 1
result = {word: count for word, count in num.items()}
print(result)

"""# **Задание 6**

Дан словарь, содержащий информацию о людях, необходимо:



*   Вывести всех людей старше 30 лет
*   Вывести список городов и количество людей из словаря проживающих в них
*   Вывести список профессий и список людей для каждой профессии

**Критерии**

Каждый из пунктов необходимо реализовать в виде функции
"""

people_info = {
    "Alice": {"age": 25, "city": "New York", "occupation": "Engineer"},
    "Bob": {"age": 30, "city": "Los Angeles", "occupation": "Designer"},
    "Charlie": {"age": 35, "city": "Chicago", "occupation": "Teacher"},
    "Diana": {"age": 28, "city": "Miami", "occupation": "Doctor"},
    "Ethan": {"age": 40, "city": "Seattle", "occupation": "Chef"},
    "Frank": {"age": 32, "city": "Atlanta", "occupation": "Lawyer"},
    "Gabriella": {"age": 29, "city": "San Francisco", "occupation": "Software Engineer"},
    "Harrison": {"age": 38, "city": "Denver", "occupation": "Architect"},
    "Isabella": {"age": 26, "city": "Washington D.C.", "occupation": "Journalist"},
    "Julian": {"age": 42, "city": "Miami", "occupation": "Musician"},
    "Kate": {"age": 31, "city": "Philadelphia", "occupation": "Nurse"},
    "Lucas": {"age": 36, "city": "Nashville", "occupation": "Businessman"},
    "Mia": {"age": 27, "city": "Atlanta", "occupation": "Artist"},
    "Natalie": {"age": 39, "city": "Portland", "occupation": "Writer"},
    "Oliver": {"age": 44, "city": "Minneapolis", "occupation": "Professor"},
    "Penelope": {"age": 33, "city": "San Diego", "occupation": "Marketing Manager"},
    "Quincy": {"age": 41, "city": "Nashville", "occupation": "Singer"},
    "Rachel": {"age": 34, "city": "Cleveland", "occupation": "Teacher"},
    "Sophia": {"age": 29, "city": "Nashville", "occupation": "Engineer"},
    "Tessa": {"age": 37, "city": "Miami", "occupation": "Lawyer"}
}
for name, info in people_info.items():
    if info["age"] > 30:
        print(name, info)

city_count = {}
for info in people_info.values():
    city = info["city"]
    if city in city_count:
        city_count[city] += 1
    else:
        city_count[city] = 1
for city, count in city_count.items():
   print(city, count)
occupation_dict = {}
for name, info in people_info.items():
    occupation = info["occupation"]
    if occupation in occupation_dict:
        occupation_dict[occupation].append(name)
    else:
        occupation_dict[occupation] = [name]
for occupation, names in occupation_dict.items():
    print(occupation, names)

"""# **Задание 7**

Задание: Разработка системы отзывов о предметах

Описание: Создать программу на Python для хранения и управления отзывами о предметах учебного курса. Программа должна позволять пользователям добавлять, просматривать и удалять отзывы, а также вычислять средний балл по заданному предмету.

**Функционал:**

*   Добавление отзыва и оценки:
   *   Пользователь может ввести название предмета, оценку (от 1 до 5) и текст отзыва.
   *   Отзывы должны храниться в структуре данных (например, словаре), где ключом будет название предмета, а значением - список отзывов (каждый отзыв может хранить оценку и комментарий).
*   Просмотр отзывов и оценок:
   *   Пользователь может запросить отзывы для указанного предмета.
   *   Если для указанного предмета есть отзывы, программа должна отобразить список всех отзывов и соответствующих оценок.
*   Удаление отзыва:
   *   Пользователь может удалить отзыв по индексу. Необходимо заранее уведомить пользователя о том, какие отзывы доступны для удаления.
   *   Программа должна обработать ситуацию, когда индекс введен неправильно.
*   Вычисление среднего балла по предмету:
   *   Пользователь может ввести название предмета, и программа должна вычислить и вывести средний балл по всем отзывам для этого предмета.
   *   Если отзывов нет, программа должна сообщить об этом.


**Критерии:**

*   Код должен быть оформлен в виде функций
*   Необходимо обрабатывать неправильный ввод пользователя
*   Должны быть комментарии к функциям
*   Присутсвует весь дополнительный функционал



**Опционально:**

Предлагаю вам добавить свои критерии оценки или вопросы, на которые должен ответить студент, чтобы оценить пару
"""

