def solution(s):
    stack = [0]*len(s)
    top = -1
    for char in s :
        if stack[top] == char : 
            top -= 1
        else : 
            top += 1
            stack[top] = char
    return 1 if top == -1 else 0