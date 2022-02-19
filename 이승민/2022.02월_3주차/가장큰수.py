def solution(numbers):
    answer = ''
    numbers = list(map(str,numbers))
    new_sorted_arr = []
    
    for arr in numbers :
        new_sorted_arr.append([arr,arr*3]) # 사전식으로 정렬하기 위해 3자리수까지 늘려준다.
        
    new_sorted_arr = sorted(new_sorted_arr,key = lambda x : x[1],reverse = True)
    
    for arr in new_sorted_arr :
        answer += arr[0]
        
    return str(int(answer))
