#Является ли строка палиндромом
def is_palindrome1(string):
    return string == ''.join(reversed(string))

print(is_palindrome1('abb'))

def is_palindrome2(string):
    return string == string[::-1]

print(is_palindrome2('abba'))