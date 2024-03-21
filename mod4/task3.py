def euclidean_algorithm(a, b):
    if b == 0:
        return a
    else:
        return euclidean_algorithm(b, a % b)

input_str = input("Введите два числа через пробел (a, b): ")
a, b = map(int, input_str.split())
result = euclidean_algorithm(a, b)
print(f"Наибольший общий делитель: {result}")