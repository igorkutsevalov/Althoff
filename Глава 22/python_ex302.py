def is_palindrome(word):
    word = word.lower()
    return word[::-1] == word


print(is_palindrome("Мама"))
print(is_palindrome("Мам"))
