# Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.
from random import randint

# формируем список друзей
friend_names = []
friend_names.append("Вася")
friend_names.append("Петя")
friend_names.append("Коля")

# формируем список всех возможных вещей
thing = []
thing.append("палатка")
thing.append("рюкзак")
thing.append("пенка")
thing.append("еда")
thing.append("вода")
thing.append("топор")
thing.append("лопата")

# формируем группу где каждый из друзей берет произвольное количество неповторяющихся для каждого вещей
group = {}

for friend in friend_names:
    thing_quantity = randint(0, len(thing)-1)
    thing_taken = []

    while thing_quantity != 0:
        j = randint(0, len(thing)-1)
        if thing[j] in thing_taken:
            pass
        else:
            thing_taken.append(thing[j])
            thing_quantity -= 1
    group[friend] = thing_taken

print(group)

# определяем список всех взятых группой вещей
all_thing = set()
for name in friend_names:
    all_thing = all_thing.union(group.get(name))

print(all_thing)

# Проверяем наличие количество вхождений каждой вещи в список вещей каждого члена команды

for current_thing in all_thing:
    count = 0
    for name in friend_names:
        if current_thing in group.get(name):
            count += 1
    # print(current_thing, " ", count)
# проверка вещей , которые взяли все
    if count == len(friend_names):
        print (f"{current_thing} - взяли все")
# проверка единственного члена группы не взявшего текущую вещь
    elif count == len(friend_names)-1:
        for name in friend_names:
            if current_thing not in group.get(name):
                print(f"только {name} не взял {current_thing}")
                break
# проверка единственного члена группы взявшего текущую вещь
    elif count == 1:
        for name in friend_names:
            if current_thing in group.get(name):
                print(f"только {name} взял {current_thing}")
                break