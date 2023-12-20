def solution(my_strings, parts):
    answer = ''
    # i = 0
    # for s,e in parts:
    #     answer += my_strings[i][s:e+1]
    #     i+=1
    # return answer
    
    for i in range(len(parts)):
        answer+=my_strings[i][parts[i][0]:parts[i][1]+1]
    return answer