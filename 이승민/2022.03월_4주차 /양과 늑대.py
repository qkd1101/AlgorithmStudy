def dfs(cur,sheep,wolf,possibility,info,link) :
    global answer
    sheep += info[cur] ^ 1 
    wolf += info[cur]
    if sheep <= wolf : 
        return
    answer = max(sheep,answer)
    possibility += link[cur]
    for idx,node in enumerate(possibility) :
        visited = []
        dfs(node,sheep,wolf,possibility[:idx]+possibility[idx+1:],info,link)
   
def solution(info, edges):
    global answer 
    answer = 0
    link = { i : [] for i in range(len(info))}
    for n1, n2 in edges:
        link[n1].append(n2)
    dfs(0,0,0,[],info,link)
    return answer