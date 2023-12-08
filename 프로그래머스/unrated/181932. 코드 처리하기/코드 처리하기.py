def toggle_mode(mode):
    return 1-mode

def solution(code):
    mode = 0
    answer = ""
    for i in range(len(code)):
        if code[i] == "1":
            mode = toggle_mode(mode)
        
        if mode==0:
            if code[i] != '1' and i%2 == 0:
                answer+=code[i]

        if mode==1:
            if code[i] != '1' and i%2 == 1:
                answer+=code[i]
    
    return "EMPTY" if answer=="" else answer