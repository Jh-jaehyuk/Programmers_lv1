def solution(n):
    answer = int(''.join([i for i in sorted(str(n),reverse=True)]))
    return answer

print(solution(118372))
