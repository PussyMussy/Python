line = input()

result = 0
for char in line:
    result += 1 if char == '1' else -1
    
print("yes" if not bool(result) else "no")