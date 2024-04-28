def is_palindrome(string):
    res = 0
    for i in range(len(string) // 2):
        if string[i] == string[-i-1]:
            res += 1
    if res == len(string) // 2:
        return True
    return False


print(is_palindrome("1232"))
