def has_duplicates(sequence):
    return len(sequence) != len(set(sequence))

# Пример использования
sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]  # Здесь есть одинаковые числа
print(has_duplicates(sequence))  # Выведет: True

sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Здесь нет одинаковых чисел
print(has_duplicates(sequence))  # Выведет: False
