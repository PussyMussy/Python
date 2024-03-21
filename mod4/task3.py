def get_greatest_common_divisor(a, b):
    return a if b == 0 else get_greatest_common_divisor(b, a % b)

a, b = map(int, input().split())
print(get_greatest_common_divisor(a, b))