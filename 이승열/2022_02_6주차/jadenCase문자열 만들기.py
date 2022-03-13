def solution(s):
    s = list(s)
    for i in range(len(s)):
        if i == 0:
            s[i] = s[i].upper()
        elif s[i - 1] == ' ' and s[i].islower():
            s[i] = s[i].upper()
        elif s[i - 1] != ' ' and s[i].isupper():
            s[i] = s[i].lower()
    return ''.join(i for i in s)
