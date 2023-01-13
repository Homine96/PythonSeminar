# Напишите программу, удаляющую из текста все слова, содержащие "абв".

from random import choices


def list_rand_words(count: int, alp: str = 'абв'):
    words_list = []
    for i in range(count):
        letters = choices(alp, k=3)
        words_list.append("".join(letters))
    return words_list

all_list = list_rand_words(int(input("Number of words: ")))
print(" ".join(all_list))


new_list=list(filter(lambda x: x != "абв", all_list))
print(" ".join(new_list))