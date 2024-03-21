def degree(a, n):
    return a if n == 1 else a * degree(a, n - 1)

a, n = map(int, input().split())
print(degree(a, n))