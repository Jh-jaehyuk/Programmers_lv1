import math
def solution(s):
    if len(s) % 2 == 1:
        answer = s[math.floor(len(s)/2)]
    else:
        answer = s[int((len(s)/2)-1)] + s[int(len(s)/2)]
    return answer

print(solution('abcde'))
print(solution('qwer'))
