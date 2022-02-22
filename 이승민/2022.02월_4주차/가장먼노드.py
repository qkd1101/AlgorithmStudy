from collections import deque
def solution(n, edge):
    count = 0
    queue = deque()
    max_depth = 0
    visited = [0]*(n+1)
    visited[1] = 1 
    dict = {}
    for i in range(1,n+1) :
        dict[i] = []
    for v1,v2 in edge :
        if v1 > v2 : v1,v2 = v2,v1 #SWAP
        if v1 == 1 : 
            visited[v2] = 1
            queue.append((v2,1))
        dict[v1].append(v2)
        dict[v2].append(v1)
    while queue : # BFS
        vertex, depth = queue.popleft()
        if max_depth < depth : 
            max_depth = depth
            count = 1
        elif max_depth == depth :
            count +=1
        for i in dict[vertex] :
            if visited[i] == 0 :
                visited[i] = 1
                queue.append((i,depth+1))
    return count