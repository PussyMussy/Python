def can_make_palindrome(word):
    char_count = {}
    for char in word:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    odd_count = 0
    odd_char = ''
    for char, count in char_count.items():
        if count % 2 != 0:
            odd_count += 1
            odd_char = char

    if odd_count > 1:
        return False

    palindrome = ''
    for char, count in char_count.items():
        palindrome += char * (count // 2)

    return palindrome + odd_char + palindrome[::-1]


word = input("Введите слово: ")
result = can_make_palindrome(word)
if result:
    print(result)
else:
    print("Из данного слова нельзя составить палиндром.")