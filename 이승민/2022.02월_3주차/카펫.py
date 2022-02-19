def solution(brown, yellow):
    answer = []
    sumOfXandY = brown//2 + 2 # 가로와 세로의 합
    div,mod = divmod(sumOfXandY,2) # 절반으로 나누어서 안떨어지면 가로를 1크게
    x = div if mod == 0 else div+1 # 가로 
    y = sumOfXandY-x # 세로 
    while y > 2 : # 가로++,세로--
        if (x-2)*(y-2) == yellow : # 조건 
            answer = [x,y]
            break
        x+=1
        y-=1
    return answer
