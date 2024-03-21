line = input()
lineLength = len(line)
newWord = ''

for i in range(lineLength):
    if line[i] == ' ':
        newWord += line[i - 1]
    if i == lineLength - 1:
        newWord += line[i]
        
print(newWord)