def get_palindrom(word):
    word = word.lower()
    counts = dict()
    for letter in word:
        counts[letter] = 1 if letter not in counts else counts[letter] + 1 
    middle = ""
    palindrom = ""
    if middle:
        malindrom = middle * counts[middle]
    for letter in counts:
        if letter != middle:
            palindrom = letter * int(counts[letter] / 2) + palindrom + letter * int(counts[letter] / 2) 
    return palindrom

word = input()
print(get_palindrom(word))