# пользователь загадывает число от 0 до 1000. Программе Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000

num = randint(LOWER_LIMIT, UPPER_LIMIT)

count = 10

print(num)

left_limit = 0
right_limit = 1000

previous_user_num = 0

while count > 0:
    user_num = (left_limit+right_limit)//2

    if user_num == previous_user_num: # проверка нахождения числа 1000, поскольку округление идет вниз
        user_num += 1                 # и в предельном случае программа застопорится на 999


    print("осталось {} попыток".format(count))
    print("выбрано", user_num)

    if num > user_num:
        print("загаданое число больше чем ", user_num)
        left_limit = user_num
    elif num < user_num:
        print("загаданое число меньше чем ", user_num)
        right_limit = user_num
    else:
        print("верно")
        quit()
    count -= 1
    previous_user_num = user_num

print("попытки за кончились")
