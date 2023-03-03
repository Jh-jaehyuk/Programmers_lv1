def solution(t, p):
    count = 0
    start = 0
    i = len(p)
    while i <= len(t):
        print(int(t[start:i]))
        if int(t[start:i]) <= int(p):
            count += 1
            i += 1
            start += 1
        else:
            i += 1
            start += 1
    return count

print(solution("500220839878", "7"))

