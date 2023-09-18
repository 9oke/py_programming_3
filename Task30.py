# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def fill_arithmetic_progression(a1, d, n):
    progression = []
    for i in range(n):
        an = a1 + i * d
        progression.append(an)
    return progression

def print_progression(progression):
    print("Элементы арифметической прогрессии:")
    for element in progression:
        print(element)

a1 = float(input("Введите первый элемент прогрессии: "))
d = float(input("Введите разность прогрессии: "))
n = int(input("Введите количество элементов прогрессии: "))

progression = fill_arithmetic_progression(a1, d, n)

print_progression(progression)