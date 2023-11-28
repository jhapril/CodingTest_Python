def solution(ineq, eq, n, m):
    n = int(n)
    m = int(m)
    if ineq==">":
        if eq == "=":
            if n>=m:
                return 1
            else :
                return 0
        else:
            if n>m:
                return 1
            else:
                return 0
    else:
        if eq == "=":
            if n<=m:
                return 1
            else:
                return 0
        else :
            if n<m:
                return 1
            else:
                return 0