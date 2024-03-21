phone_number_format = input()
phone_number = ''

for char in phone_number_format:
    if char == '-' or char == ')' or char == '(' or char == ' ':
        continue
    phone_number += char
    
print(phone_number)