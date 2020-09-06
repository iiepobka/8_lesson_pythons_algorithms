# Закодируйте любую строку по алгоритму Хаффмана.
from collections import Counter

arr = []


def object_iter(array):
    for z in array:
        if isinstance(z, list):
            object_iter(z)
        else:
            arr.append(z)
    return arr


def bubble_sort(array):
    len_arr = 1
    count = 0
    while count < len(array):
        for i in range(len(array) - len_arr):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                keys[i], keys[i + 1] = keys[i + 1], keys[i]
        len_arr += 1
        count += 1
    return array


with open('war_and_peace.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# 'beep boop beer!' итоговый ответ отличается от того, что в методичке, но на вебинаре
# было сказано, что нет разницы в какой последовательности стоят символы, главное, чтобы
# была сортировка по частоте вхождения символов (по крайней мере у меня получился другой
# ответ из-за того, что на промежуточном уровне иначе стоят буквы, но частота вхождения
# у них одинаковая)
user_row = text  # input('Введите любую строку: ')

keys = list(Counter(user_row).keys())
values = list(Counter(user_row).values())
bubble_sort(values)
result_dict = {k: [] for k in keys}

while len(values) != 1:
    if values[1] >= values[0]:
        left = object_iter(keys[0])
        for el in left:
            result_dict[el] += [0]
        else:
            arr.clear()
        right = object_iter(keys[1])
        for el in right:
            result_dict[el] += [1]
        else:
            arr.clear()
        values[1] = values[0] + values[1]
        keys[1] = [keys[0], keys[1]]
        del values[0]
        del keys[0]
    bubble_sort(values)

haffman_row = []
for l in user_row:
    if l in result_dict:
        haffman_row.extend([result_dict[l]])
haffman_row = str(haffman_row)
with open('war_and_peace_haffman.txt', 'w', encoding='utf-8') as f:
    f.write(haffman_row)

