def solution(s):
    s_list = list(s)
    stack = []
    for c in s_list :
        if not stack : 
            stack.append(c)
        else :
            if c == '(' :
                stack.append(c)
            else :
                if stack[-1] == '(' :
                    stack.pop()
    return True if not stack else False