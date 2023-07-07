# Напишите программу, которая получает целое число
# и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

result = ""
number = int(input ("введите целое число: "))
init_number = number
base = 16

while number > 0:
    match (number % base):
        case 10:
            add = "a"
        case 11:
            add = "b"
        case 12:
            add = "c"
        case 13:
            add = "d"
        case 14:
            add = "e"
        case 15:
            add = "f"
        case _:
            add = str(number % base)

    result = add + result
    number = number // base
print(init_number, "в шестнадцатерично системе = ", result)

print("проверка", hex(init_number)[2:])
