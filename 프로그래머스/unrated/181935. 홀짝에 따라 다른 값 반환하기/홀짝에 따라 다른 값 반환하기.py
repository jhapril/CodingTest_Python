def solution(n):
    # if n%2 != 0:
    #     sum1 = 0
    #     for i in range(1, n+1, 2):
    #         sum1 += i
    #     return sum1
    # elif n%2 == 0:
    #     sum2 = 0
    #     for i in range(0, n+1 ,2):
    #         sum2 += i*i
    #     return sum2
    
    if n%2 != 0:
        sum1 = 0
        while n>0:
            sum1 += n
            n -= 2
        return sum1
    elif n%2 == 0:
        sum2 = 0
        while n>0:
            sum2 += n*n
            n -= 2
        return sum2