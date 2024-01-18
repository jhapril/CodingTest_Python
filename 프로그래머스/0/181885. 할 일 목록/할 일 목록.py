def solution(todo_list, finished):
    answer = []
    # for a,b in zip(todo_list, finished):
    #     if b == 0:
    #         answer.append(a)
    # return answer

    for i in range(len(finished)):
        if finished[i] == 0:
            answer.append(todo_list[i])
    return answer