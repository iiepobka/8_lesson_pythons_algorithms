# Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных
# подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.

def sub_row_counter_with_hash(row):
    hash_list = []
    count = 1
    subtrahend = 0
    while True:
        for i in range(len(row) - subtrahend):
            if hash(row[i: i + count]) not in hash_list:
                hash_list.append(hash(row[i: i + count]))
        count += 1
        subtrahend += 1
        if hash_list[-1] == hash(row):
            del hash_list[- 1]
            break

    return f'{len(hash_list)} подстрок[и|а] в строке "{row}"'


user_row = input('Введите любую строку: ')
print(sub_row_counter_with_hash(user_row))
