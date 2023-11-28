def solution(a, b):
    a = str(a)
    b = str(b)
    c = a+b
    d = b+a
    c = int(c)
    d = int(d)
    if c > d :
        answer = c
    else:
        answer = d
    return answer