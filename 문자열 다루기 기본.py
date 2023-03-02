def solution(s):
    if len(s) == 4 or len(s) == 6:
        if s.isdigit():
            answer = True
        else:
            answer = False
    else:
        answer = False
    # return s.isdigit() and len(s) in [4, 6]
    return answer

print(solution('1234'))
