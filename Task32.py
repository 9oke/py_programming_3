# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума). Список можно задавать рандомно

# На входе : [ 1, 5, 88, 100, 2, -4]
# 33
# 200
# Ответ: [2, 3]

import random

n = int(input("Введите размер списка: "))
min_value = int(input("Введите минимальное значение диапазона: ")) 
max_value = int(input("Введите максимальное значение диапазона: ")) 

random_list = [random.randint(min_value, max_value) for _ in range(n)]

print("Список:", random_list)

search_min = int(input("Введите минимальное значение диапазона поиска: "))
search_max = int(input("Введите максимальное значение диапазона поиска: "))

indices = [i for i, value in enumerate(random_list) if search_min <= value <= search_max]

print("Индексы элементов в заданном диапазоне:", indices)