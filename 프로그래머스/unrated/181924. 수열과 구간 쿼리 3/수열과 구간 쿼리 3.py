def solution(arr, queries):
    temp = ""
    for i, j in queries:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
    return arr