# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел
# для случайной расстановки ферзей в задаче выше. Проверяйте различный случайные
# варианты и выведите 4 успешных расстановки.

from random import randint
from HW06.task02.chess import validate_queens


def generate_positions():
    count = 0
    while count < 4:
        positions = list((j+1,  randint(1, 8)) for j in range(8))  # создаём список с числами от 1 до 8
        if validate_queens(positions):
            print(positions)
            count += 1


generate_positions()

# E:\Python_seminars\Lesson1\homework\venv\Scripts\python.exe E:\Python_seminars\Lesson1\homework\HW06\task03\main.py
# [(1, 5), (2, 2), (3, 4), (4, 7), (5, 3), (6, 8), (7, 6), (8, 1)]
# [(1, 8), (2, 2), (3, 4), (4, 1), (5, 7), (6, 5), (7, 3), (8, 6)]
# [(1, 3), (2, 6), (3, 4), (4, 1), (5, 8), (6, 5), (7, 7), (8, 2)]
# [(1, 3), (2, 6), (3, 4), (4, 2), (5, 8), (6, 5), (7, 7), (8, 1)]
#
# Process finished with exit code 0