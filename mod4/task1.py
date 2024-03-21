def check_numbers(numbers):
    unique_numbers = set(numbers)
    if len(unique_numbers) == 1:
        print("Все числа равны")
    elif len(unique_numbers) == len(numbers):
        print("Все числа разные")
    else:
        print("Есть равные и неравные числа")

input_numbers = input("Введите числа через пробел: ")
numbers_list = list(map(int, input_numbers.split()))
check_numbers(numbers_list)
