# Напишите программу, которая принимает две строки вида “a/b”
# - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions

from fractions import Fraction

def gcd_user(a,b):
    while b != 0:
        a, b = b, a % b
    return a

print("слоджение и умножение натуральных дробей")
numerator1, denominator1 = input("введите первую натуральную дробь вида a/b: ").split("/")
numerator2, denominator2 = input("введите вторую натуральную дробь вида a/b: ").split("/")

numerator1 = int(numerator1)
denominator1 = int(denominator1)
numerator2 = int(numerator2)
denominator2 = int(denominator2)

# проводим сложение двух дробей
summ_num = numerator1 * denominator2 + numerator2 * denominator1
summ_denom = denominator2 * denominator1

res_summ_num = int(summ_num / gcd_user(summ_num, summ_denom))
res_summ_denom = int(summ_denom / gcd_user(summ_num, summ_denom))

print(f"сумма двух дробей = : {res_summ_num}/{res_summ_denom}")
print("проверка методом Fractions: ", Fraction(numerator1, denominator1)+Fraction(numerator2, denominator2))

# проводим умножение  двух дробей
mult_num = numerator1 * numerator2
mult_denom = denominator2 * denominator1

res_mult_num = int(mult_num / gcd_user(mult_num, mult_denom))
res_mult_denom = int(mult_denom / gcd_user(mult_num, mult_denom))

print(f"произведение двух дробей = : {res_mult_num}/{res_mult_denom}")
print("произведение методом Fractions: ", Fraction(numerator1, denominator1)*Fraction(numerator2, denominator2))

