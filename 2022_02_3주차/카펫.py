def solution(brown, yellow):
    answer = []
    layer = 1
    while True:
        if yellow/layer*2+4+layer * 2 == brown:
            break
        else:
            layer += 1
    answer.append(yellow/layer+2)
    answer.append(layer + 2)
    return answer
