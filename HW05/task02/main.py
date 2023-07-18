# Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.


def path_to_tuple(user_string):
    *a, b = user_string.split("/")
    a = "/".join(a)+"/"
    b, c = b.split(".")
    result = (a, b, c)
    return result

user_string = "E:/3d/toys/form.stl"
print(path_to_tuple(user_string))