# Напишите функцию для транспонирования матрицы
from random import randint

def matrix_generation(rows: int, columns: int):
    matrix = []
    for i in range(rows):
        matrix_column = []
        for j in range(columns):
            matrix_column.append(None)
        matrix.append(matrix_column)
    return matrix

def fill_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = randint(0, 99)

def matrix_print(matrix):
    for i in range(len(matrix)):
        print(matrix[i])
    print("\n")
def matrix_transpons(matrix):
    t_matrix = matrix_generation(len(matrix[0]), len(matrix))

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            t_matrix[len(matrix[0])-j-1][i] = matrix[i][j]
    return t_matrix


rows = 10
columns = 5

# создаем пустую матрицу заданных размеров
matrix = matrix_generation(rows, columns)
# заполняем матрицу произвольными целыми часками от 0 до 99
fill_matrix(matrix)
# печатаем матрицу
matrix_print(matrix)
# транспонируем             )
t_matrix = matrix_transpons(matrix)
# печатаем транспонированную матрицу
matrix_print(t_matrix)