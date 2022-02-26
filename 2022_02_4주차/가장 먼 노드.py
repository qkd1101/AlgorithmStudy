from collections import deque


def solution(n, edge):
    # 리스트 대신 딕셔너리를 이용하여 adj list 형태로 구현한다.
    graph = {}

    # 딕셔너리도 각각 리스트 형태로
    for i in range(1, n + 1):
        graph[i] = []

    # 딕셔너리에 값 넣기
    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    visited = [0]*(n+1)
    visited[1] = 1
    queue = deque([1])  # 큐에 시작노드 넣기

    while(queue):
        v = queue.popleft()
        # list인 queue에서 pop() 이랑 동일
        # 왼쪽 끝 요소를 가져오는 동시에 데크에서 삭제

        for i in graph[v]:
            if visited[i] == 0:
                visited[i] = visited[v] + 1
                queue.append(i)
        # max() : 배열들에서 최대값 가져옴
        # 배열.count(element) : 배열들 중 element인 개수 세아림
    return visited.count(max(visited))
