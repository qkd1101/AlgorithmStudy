def solution(clothes):
    answer = 1
    d = {}
    # 경우의 수로 접근을 위해 key 당 입을 수 있는 옷 수: value
    for i in clothes:
        if i[1] in d:
            d[i[1]] += 1
        else:
            d[i[1]] = 1
    # 안입는 경우까지 생각해서 + 1, 아무것도 안입는 경우 없음 - 1
    for i in d.keys():
        answer *= (d[i] + 1)
    return answer - 1
