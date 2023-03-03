from itertools import combinations
def solution(numbers):
    answer = sorted(list(set([sum(i) for i in list(combinations(numbers, 2))])))
    return answer

print(solution([2,1,3,4,1]))
