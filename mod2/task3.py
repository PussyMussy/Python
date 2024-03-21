def sort_and_find_middle(a, b, c):
    # Сортировка чисел по возрастанию
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b

    # Определение числа, стоящего между двумя другими
    middle_number = b

    return a, middle_number, c

# Ввод трех чисел
a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
c = float(input("Введите число c: "))

# Вызов функции и вывод результата
sorted_a, middle, sorted_c = sort_and_find_middle(a, b, c)
print("Упорядоченные числа:", sorted_a, middle, sorted_c)
print("Число, стоящее между двумя другими:", middle)
