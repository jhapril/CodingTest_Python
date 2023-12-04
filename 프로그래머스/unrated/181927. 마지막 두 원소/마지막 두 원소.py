def solution(num_list):
    a, b = num_list[-1], num_list[-2]
    if a>b:
        num_list.append(a-b)
    else :
        num_list.append(2*a)
    return num_list