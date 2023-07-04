# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: «Число является простым, если делится нацело только на единицу
# и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

number = None
flag = False

while not flag:
    number = input("введите положительное целое число от 2 до 100000: ")
    flag = number.isdigit()
    if flag:
        if 1 < int(number) < 100000:
            pass
        else:
            flag = False

number = int(number)

for i in range (2, int(number/2)+1):
    if number % i == 0:
        print("число {} не является простым".format(number))
        quit()

print("число {} является простым".format(number))