def extract_last_letters(word_list):
    result_word = ''
    for word in word_list:
        if len(word) > 0:  # Проверка, что слово не пустое
            last_letter = word[-1]  # Извлечение последней буквы
            result_word += last_letter  # Добавление последней буквы к результату
    return result_word

# Ввод списка слов
word_list = input("Введите список слов через пробел: ").split()

# Вызов функции и вывод результата
result = extract_last_letters(word_list)
print("Новое слово из последних букв каждого слова:", result)
