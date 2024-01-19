def solution(before, after):
    before, after = list(before), list(after)
    for i in before:
        if i in after:
            after.remove(i)
    return 1 if len(after)==0 else 0