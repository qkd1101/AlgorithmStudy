from collections import deque

def bfs(node,count,arr,visited,n) :
    queue = deque()
    visited[node] = 1
    queue.append(node)
    while queue :
        node = queue.popleft()
        for i in range(1,n+1) :
            if arr[node][i] == 1 and visited[i] == 0 :
                queue.append(i)
                count+=1
                visited[node] = 1
    return count

def solution(n, wires):
    min_val = 10**5
    arr = list([0] * (n+1) for _ in range(n+1))
    for x,y in wires :
        arr[x][y],arr[y][x] = 1,1
    for x,y in wires :
        arr[x][y],arr[y][x] = 0,0
        min_val = min(min_val,abs(bfs(x,1,arr,[0]*(n+1),n) - bfs(y,1,arr,[0]*(n+1),n)))
        arr[x][y],arr[y][x] = 1,1
    return min_val