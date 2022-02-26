import math
from itertools import permutations

# 소수 찾기


def primeNumber(x):
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True
# 숫자 뽑기


def select(items, num):
    count = 0
    # 순열로 뽑고 int로 변환
    str_list = list(map(''.join, permutations(items, num)))
    int_list = list(map(int, str_list))
    return int_list


def solution(numbers):
    answer = 0
    all_list = []
    for i in range(1, len(numbers) + 1):
        all_list += select(numbers, i)

    # 중복 제거하기
    set_list = set(all_list)
    all_list = list(set_list)

    # count
    for i in all_list:
        if primeNumber(i) and i > 1:
            print(i)
            answer += 1

    return answer
