from collections import deque

def solution(bridge_length, weight, truck_weights):
    queue = deque()
    time = 1
    idx = 0
    truck_sum = 0
    truck_num = len(truck_weights)
    queue.append([truck_weights[0],bridge_length])
    truck_sum += truck_weights[0]
    idx += 1
    while queue : 
        if time == queue[0][1] : 
            poped = queue.popleft()
            truck_sum -= poped[0]          
        if idx < truck_num and truck_sum+truck_weights[idx] <= weight :
            queue.append([truck_weights[idx],time+bridge_length])
            truck_sum += (truck_weights[idx])
            idx += 1
        time += 1
    return time