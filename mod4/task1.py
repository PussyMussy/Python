def check_numbers(numbers):
    uniqueLen = len(list(set(numbers)))
    if uniqueLen == 1:
        print("Все числа равны")
    elif uniqueLen < len(numbers):
        print("Есть равные и неравные числа")
    else:
        print("Все числа разные")
         
numbers = list(map(int, input().split()))
check_numbers(numbers)
