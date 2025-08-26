def check_palindrome(s):
    if len(s) <= 1:
        return 'true'
    if s[0] == s[:-1]:
        return check_palindrome(s[1:-1])
    else:
        return 'false'


s = input()
print(check_palindrome(s))
