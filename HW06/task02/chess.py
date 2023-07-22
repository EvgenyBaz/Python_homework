#
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг
# друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара
# бьющих друг друга. Программа получает на вход восемь пар чисел, каждое число от
# 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если
# бьют - ложь.

def validate_queens(positions):
    result = True
    for i in range(len(positions)):
        row_1, col_1 = positions[i]
        for j in range(i + 1, len(positions)):
            row_2, col_2 = positions[j]
            # проверка на наличие на одной строке или диагонали
            if row_1 == row_2 or col_1 == col_2 or abs(row_1 - row_2) == abs(col_1 - col_2):
                result = False
                break
    return result


if __name__ == "__main__":
    positions = [(4,1), (8,2), (1,3), (3,4), (6,5), (2,6), (7,7), (5,8)]
    print(validate_queens(positions))