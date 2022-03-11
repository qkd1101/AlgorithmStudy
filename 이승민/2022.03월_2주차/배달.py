
################  bfs 변형 visited 없애고, 모든 노드 방문하면서 더이상 dist를 갱신할 수 없을 때 까지

from collections import deque
def solution(N, road, K):
    queue = deque()
    MAX = 500000
    dist = [MAX]*(N+1)
    answer = 0
    edge = {}
    for node1,node2,w in road :
        if edge.get(node1) == None :
            edge[node1] = [(node2,w)]
        else :
            edge[node1].append((node2,w))
        if edge.get(node2) == None :
            edge[node2] = [(node1,w)]
        else :
            edge[node2].append((node1,w))
    
    queue.append((1,0))
    dist[1] = 0
    while queue :
        cur_node,cur_weight = queue.popleft()
        for next_node,next_weight in edge[cur_node] :
            if dist[next_node] > cur_weight + next_weight :
                dist[next_node] = cur_weight + next_weight
                queue.append((next_node,dist[next_node]))
                
    return sum(1 for d in dist if d <= K)

################  다익스트라 - findMin 선형 탐색  O(v^2)

def findMin(dist,visited) :
    w = 500000
    for idx,weight in enumerate(dist) :
        if weight < w and not visited[idx] :
            w = weight
            n = idx
    return (n,w)

def dijkstra(start,edge,dist,N) :
    visited = [0]*(N+1)
    dist[start] = 0
    for _ in range(N-1) :
        cur_node,cur_weight = findMin(dist,visited)
        visited[cur_node] = 1
        for next_node,next_weight in edge[cur_node] :
            if cur_weight + next_weight < dist[next_node] :
                dist[next_node] = cur_weight + next_weight
                
def solution(N, road, K):
    MAX = 500000
    dist = [MAX]*(N+1)
    edge = {}
    for node1,node2,w in road :
        if edge.get(node1) == None :
            edge[node1] = [(node2,w)]
        else :
            edge[node1].append((node2,w))
        if edge.get(node2) == None :
            edge[node2] = [(node1,w)]
        else :
            edge[node2].append((node1,w))
    
    dijkstra(1,edge,dist,N)
                
    return sum(1 for d in dist if d <= K)

################  다익스트라 - findMin 우선수위 큐  O(vlogv)

import heapq

def dijkstra(start,edge,dist) :
    heap = []
    heapq.heappush(heap,(0,start))
    dist[start] = 0
    while heap :
        cur_weight,cur_node = heapq.heappop(heap)
        if dist[cur_node] != cur_weight : # 이미 최신화 되어서 바뀐 경우
            continue
        for next_weight,next_node in edge[cur_node] :
            if dist[next_node] > cur_weight + next_weight :
                dist[next_node] = cur_weight + next_weight
                heapq.heappush(heap,(dist[next_node],next_node))

def solution(N, road, K):
    edge = {}
    answer = 0
    dist = [500000]*(N+1)
    for node1,node2,weight in road :
        if edge.get(node1) : 
            edge[node1].append((weight,node2))
        else :
            edge[node1]=[(weight,node2)]
        if edge.get(node2) : 
            edge[node2].append((weight,node1))
        else :
            edge[node2]=[(weight,node1)]

    dijkstra(1,edge,dist)

    return sum(1 for d in dist if d <= K )
