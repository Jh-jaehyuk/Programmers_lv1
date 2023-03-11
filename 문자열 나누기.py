def solution(s):
    answer = 1
    a = 0
    b = 0
    start = s[0]
    for i in range(len(s)-1):
        if s[i] == start:
            a += 1
        else:
            b += 1

        if a == b:
            answer += 1
            a = 0
            b = 0
            start = s[i+1]

    return answer

print(solution('banana'))

