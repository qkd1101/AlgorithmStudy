def clothesPair(depth,lens,pair,dic,keys,res) :
    count = 0
    if depth == lens :
        return res
    pair[depth] = 0
    count += clothesPair(depth+1,lens,pair,dic,keys,res)
    pair[depth] = 1
    count += clothesPair(depth+1,lens,pair,dic,keys,res*dic[keys[depth]])
    return count
    
def solution(clothes):
    dic = {}
    for cloth,key in clothes : 
        if dic.get(key) : dic[key] +=1
        else : dic[key] = 1
    keys = list(dic.keys())
    lens = len(keys)
        
    return clothesPair(0,lens,[0]*lens,dic,keys,1)-1  # [0,0,...,0,0] 인경우