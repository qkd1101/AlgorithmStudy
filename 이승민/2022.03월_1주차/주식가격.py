def solution(prices):
    answer = []
    lens = len(prices)
    for i in range(0,lens) :
        cnt = 0
        for j in range(i+1,lens) :
            cnt += 1
            if prices[i] > prices[j] :
                break
        answer.append(cnt)
    return answer