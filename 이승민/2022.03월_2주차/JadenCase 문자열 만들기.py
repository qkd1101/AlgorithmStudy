def solution(s):
    answer = ''
    s_list = s.split(" ")
    for word in s_list :
        if word == "" :
            answer += " "
        else :
            answer += (word[0].upper() + word[1:].lower() + " " )
    return answer[:-1]