line = input()
char = line[len(line) - 1]

result = 0
for c in line:
    if c == ',' or c != char:
        break;
    result += 1

print(result)