def solution(num_list):
    answer1 = ''
    answer2 = ''
    for i in range(len(num_list)):
        if num_list[i] % 2 == 1:
            answer1 += str(num_list[i])
        elif num_list[i] % 2 == 0:
            answer2 += str(num_list[i])
    answer1 = int(answer1)
    answer2 = int(answer2)
    return answer1+answer2