# Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.
my_list = [1, 2, 1, 2, 3, 5, 3, 4, 5, 6, 3]
i = 0
new_list = []
while i < len(my_list):
    if my_list.count(my_list[i]) > 1:
        temp = my_list[i]
        for j in range(my_list.count(temp)):
            my_list.remove(temp)
        new_list.append(temp)
    else:
        i += 1
print(my_list)
print(new_list)
