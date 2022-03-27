from collections import deque

def solution(maps):
    answer = -1
    row,col = len(maps),len(maps[0])
    queue = deque()
    queue.append((0,0,1))
    visited = [[0]*col for _ in range(row)]
    visited[0][0] = 1
    while queue :
        x,y,depth = queue.popleft()
        if (x,y) == (row-1,col-1) :
            return depth
        for dx,dy in (1,0),(0,1),(0,-1),(-1,0) :
            nx,ny = x+dx,y+dy
            if 0<=nx<row and 0<=ny<col and maps[nx][ny] != 0 and visited[nx][ny] ==0 :
                visited[nx][ny] = 1
                queue.append((nx,ny,depth+1))
    return -1