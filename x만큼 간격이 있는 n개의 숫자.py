def solution(x, n):
    answer = [x+x*(i-1) for i in range(1, n+1)]
    return answer
# 등차수열을 생각하면 간단함.
print(solution(2, 5))
