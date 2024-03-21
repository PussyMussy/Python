def clean_phone_number(phone_number):
    # Удаление всех символов, кроме плюса и цифр
    cleaned_number = ''.join(filter(lambda x: x.isdigit() or x == '+', phone_number))
    return cleaned_number

# Ввод номера телефона
input_number = input("Введите номер телефона: ")

# Очистка номера телефона и вывод результата
cleaned_number = clean_phone_number(input_number)
print("Очищенный номер телефона:", cleaned_number)
