from itertools import combinations
def is_prime_number(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def solution(nums):
    answer = []
    l = list(combinations(nums, 3))
    sum_l = [sum(i) for i in l]
    for i in sum_l:
        if is_prime_number(i):
            answer.append(i)
    return len(answer)

print(solution([1,2,7,6,4]))
