def solution(num_list):
    # answer1, answer2, answer3 = 1,0,0
    # for i in range(len(num_list)):
    #     answer1 *= num_list[i]
    #     answer2 += num_list[i]
    # answer3 = answer2*answer2
    # if answer1<answer3:
    #     return 1
    # if answer1 > answer3:
    #     return 0
    answer1, answer2, answer3 = 1,0,0
    for i in num_list:
        answer1*=i
        answer2+=i
    answer3 = answer2**2
    if answer1<answer3:
        return 1
    elif answer1>answer3:
        return 0