from collections import deque
def solution(n, computers):
    queue = deque()
    answer = 0
    visited = [0]*n
    for i in range(len(computers)) :
        for j in range(len(computers[i])) :
            if computers[i][j] == 1 and visited[j] == 0 :
                visited[i] = 1
                queue.append(i)
                while queue : 
                    pop = queue.popleft()
                    for k in range(len(computers[pop])) : 
                        if computers[pop][k] == 1 and visited[k] == 0 :
                            visited[k] = 1
                            queue.append(k)                  
                answer += 1    
    return answer