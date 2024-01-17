def solution(arr, query):
    for i,value in enumerate(query):
        if i%2 != 0:
            arr = arr[value:]
        else :
            arr = arr[:value+1]
    return arr