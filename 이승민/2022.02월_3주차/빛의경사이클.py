def solution(grid):
    answer = []
    
    grid = list(map(list,grid)) # 문자열 리스트를 각 좌표로 리스트로 변환
    
    row = len(grid)-1 # 세로길이
    
    col = len(grid[0])-1 # 가로길이
    
    direction = { # ex) 'R' 노드에 (1,0) 방향의 빛이 들어오면 다음 빛의 방향 (0,-1)을 알려주기 위한 용도
        'R' : {
            (1,0) : (0,-1),
            (-1,0) : (0,1),
            (0,-1) : (-1,0),
            (0,1) : (1,0)
        } , 
        'L' : {
            (1,0) : (0,1),
            (-1,0) : (0,-1),
            (0,-1) : (1,0),
            (0,1) : (-1,0)
        },
        'S' : {
            (1,0) : (1,0),
            (-1,0) : (-1,0),
            (0,-1) : (0,-1),
            (0,1) : (0,1)
        }
    }
    
    pair = { # visited (x,y)좌표의 노드에서 아래 key값의 방향으로 빛이 나간적이 있는가를 체크하기 위한 용도
        (1,0) : 0,
        (-1,0) : 1,
        (0,-1) : 2,
        (0,1) : 3
    }
    
    visited = {}
    
    for x in range(row+1) :
        for y in range(col+1) :
            visited[(x,y)] = [0,0,0,0] # 모든 좌표에 빛이 들어왔던 4가지 방향을 체크 하기 위해 # 아래,위,왼,오
            
    for i in range(row+1) :
        for j in range(col+1) :
            for dir in (1,0),(-1,0),(0,-1),(0,1) : # 모든 좌표에서 4가지 방향으로 빛을 쏜다
                start = (i,j) # while문 이후 순환을 체크하기 위한 용도
                start_dir = dir # while문 이후 순환을 체크하기 위한 용도
                cnt = 0
                cur = (i,j)
                
                while visited[cur][pair[dir]] == 0 :
                    x,y = cur
                    visited[cur][pair[dir]] = 1 # 현 좌표에서 들어온 빛의 방향 방문 체크
                    dx,dy = direction[grid[x][y]][dir] # 다음 빛의 방향
                    nx,ny = x+dx,y+dy # 다음 방문 좌표
                    if nx < 0 : # 왼쪽 끝 
                        nx = row
                    if nx > row : # 오른 쪽 끝
                        nx = 0
                    if ny < 0 : # 위의 끝
                        ny = col
                    if ny > col : # 아래의 끝
                        ny = 0
                    dir = (dx,dy) # 다음 빛의 방향 설정
                    cur = (nx,ny) # 다음 방문 좌표 설정
                    cnt+=1
                    
                if start == cur and start_dir == dir and cnt != 0 : # 순환으로 인해 종료 했을 경우 
                    answer.append(cnt)

    return sorted(answer) # 오름차순
