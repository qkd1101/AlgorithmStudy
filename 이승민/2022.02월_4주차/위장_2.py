
# 1번 테스트 케이스 시간 초과 존나게 떠서 결국 질문 사항 보고 해결함 ㅅㅂ..ㅋ
def solution(clothes):
    dic = {}
    for cloth,key in clothes : 
        if dic.get(key) : dic[key] +=1
        else : dic[key] = 1
    res = 1
    for key in dic.keys() :
        res *= (dic[key]+1) # (해당 종류의 옷의 개수 + 안입은 경우의 수)
    return res-1  # 아무것도 안입은 경우 -1