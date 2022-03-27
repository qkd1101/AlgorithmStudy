def solution(n):
    answer = 0
    if n < 2 :
        return n
    prev = 0
    cur = 1
    for i in range(2,n) :
        prev,cur = cur%1234567,(prev+cur)%1234567
    return (prev+cur)%1234567