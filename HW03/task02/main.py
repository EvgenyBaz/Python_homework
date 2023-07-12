# В большой текстовой строке подсчитать количество встречаемых
# слов и вернуть 10 самых частых. Не учитывать знаки препинания
# и регистр символов. За основу возьмите любую статью
# из википедии или из документации к языку.

user_string = input("введите строку: ").lower()
chars_to_replace = "+-—.,;:!?,'"""
num_of_often_words = 10
# удаляем все знаки препинания
for char in chars_to_replace:
    user_string = user_string.replace(char, " ")
#разбиваем строку в список по пробелам
word_list = user_string.split(" ")

#удаляем все Эпустые элементы из списка
empty_char_quantity = word_list.count("")

for i in range(empty_char_quantity):
    word_list.remove("")

# получаем множество содержащее уникальные слова
all_words_set = set(word_list)

# создаем словарь ключ слово - значение - количество слов
word_dict = {}

for word in all_words_set:
    word_dict[word] = word_list.count(word)

# проходим по словарю и находим максимальное значение
for i in range (num_of_often_words):
    max_count = 0
    current_key = ""
    for word in all_words_set:

        if word_dict.get(word) > max_count:
            max_count = word_dict.get(word)
            current_key = word
    print(f"{i+1} место часто встречающихся слов занимает {current_key}. Встречается в тексте {word_dict.get(current_key)} раз")
    del word_dict[current_key]
    all_words_set.remove(current_key)




