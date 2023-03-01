def solution(n):
    answer = sum(list([int(i) for i in str(n)]))
    return answer

print(solution(987))
