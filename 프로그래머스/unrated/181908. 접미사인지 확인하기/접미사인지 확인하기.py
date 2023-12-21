def solution(my_string, is_suffix):
    # flag = 0
    # for i in range(len(my_string)):
    #     if my_string[i:] == is_suffix:
    #         flag = 1
    # return flag
    
    return int(my_string[-len(is_suffix):] == is_suffix)