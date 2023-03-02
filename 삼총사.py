from itertools import combinations
def solution(number):
    answer = 0
    a = list(combinations(number, 3))
    for i in a:
        if sum(i) == 0:
            answer += 1
    return answer

print(solution([-1, 1, -1, 1]))
