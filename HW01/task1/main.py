# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c —
# стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой
# двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника
# с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним,
# равнобедренным или равносторонним.

def input_parametr(str_param):
    while True:
        param = input("введите длину стороны  {} : ".format(str_param))
        try:
            param = float(param)
        except:
            print("{} должно быть числом".format(str_param))
        else:
            if param > 0:
                return param
            else:
                print("{} должно быть положительным числом".format(str_param))

print("введите стороны треугольника а, b, c")

side_a = input_parametr("а")
side_b = input_parametr("b")
side_c = input_parametr("c")

if side_a >= side_b+side_c or side_b >= side_a+side_c or side_c >= side_b+side_a:
    print("треугольник не существует")

else:
    print("треугольник существует")
    if side_a == side_b == side_c:
        print("треугольник равносторонний")
    elif side_a == side_b or side_a == side_c or side_c == side_b:
        print("треугольник равнобедренный")

