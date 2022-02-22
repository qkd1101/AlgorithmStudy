import itertools

def tupleToInt(tup) :
    return int(''.join(tup))

def isPrime(num) :
    if num==0 or num==1 :
        return False  
    for i in range(2,num//2+1) :
        if num%i == 0 :
            return False
    return True

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    numList = []
    lens = len(numbers)
    for i in range(1,lens+1) :
        numList.append(list(map(tupleToInt,set(itertools.permutations(numbers,i)))))
    numList = list(set(itertools.chain(*numList)))
    for num in numList : 
        if isPrime(num) : answer+=1
    return answer