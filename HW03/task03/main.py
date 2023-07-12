# Создайте словарь со списком вещей для похода в качестве
# ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант.

things = {}
things["еда"] = 3
things["вода"] = 2
things["одежда"] = 3
things["инвентарь"] = 4
things["палатка"] = 5

taken_things = []

max_weight = 10

weight_left = max_weight

for key in things:
    if weight_left - things.get(key) >= 0:
        taken_things.append(key)
        weight_left -= things.get(key)

if not taken_things:
    print ("в рюкзак ничего не влезло")
else:
    print(f"в рюкзак поместилось {taken_things}")



