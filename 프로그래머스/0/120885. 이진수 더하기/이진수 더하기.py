def solution(bin1, bin2):
    answer = ''
    bin1, bin2 = list(bin1), list(bin2)
    def square(list):
        temp = 0
        for i, val in enumerate(reversed(list)):
            temp += int(val)*(2**i)
        return temp
    temp1 = square(bin1)
    temp2 = square(bin2)
    temp3 = temp1 + temp2
    if temp3 == 0:
        return "0"
    else :
        while temp3!=1:
            answer = str(temp3%2)+answer
            temp3 //= 2
        return str(1) + answer