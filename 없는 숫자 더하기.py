def solution(numbers):
    answer = sum([i for i in range(0, 10) if i not in numbers])
    return answer

print(solution([5,8,4,0,6,7,9]))
