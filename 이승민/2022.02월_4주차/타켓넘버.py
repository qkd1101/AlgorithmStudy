import sys
sys.setrecursionlimit(10**8)

def dfs(numbers,target,lens,depth,sum) :
    if depth == lens :
        if sum == target : return 1
        return 0
    number = numbers[depth]
    return dfs(numbers,target,lens,depth+1,sum-number) + dfs(numbers,target,lens,depth+1,sum+number)

def solution(numbers, target):
    return dfs(numbers,target,len(numbers),0,0)