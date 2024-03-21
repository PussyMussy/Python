def count_ones_and_zeros(input_string):
    count_ones = 0
    count_zeros = 0
    for char in input_string:
        if char == '0':
            count_zeros += 1
        elif char == '1':
            count_ones += 1
    return count_ones == count_zeros

# Ввод строки
input_str = input("Введите строку, состоящую из 0 и 1: ")

# Проверка и вывод результата
if count_ones_and_zeros(input_str):
    print('yes')
else:
    print('no')
