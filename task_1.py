# Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных
# подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.

def sub_row_counter_with_hash(row):
    hash_list = set()
    count = 1
    subtrahend = 0
    while count < len(row):
        for i in range(len(row) - subtrahend):
            hash_list.add(hash(row[i: i + count]))
        count += 1
        subtrahend += 1


    return f'{len(hash_list)} подстрок[и|а] в строке "{row}"'


user_row = input('Введите любую строку: ')
print(sub_row_counter_with_hash(user_row))
