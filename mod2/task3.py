line = input()
lineLength = len(line)
numbersList = []
numberTemp = ''

for char in enumerate(line):
    if char[1] != ' ':
        numberTemp += char[1]
        if char[0] != lineLength - 1:
            continue
    numbersList.append(numberTemp)
    numberTemp = ''

a, b, c = numbersList;

if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
print(b)
