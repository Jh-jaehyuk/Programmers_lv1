def is_prime_number(n):
    for i in range(2, int(n**0.5+1)):
        if n % i == 0:
            return False
    return True

def solution(n):
    answer = []
    for i in range(2, n+1):
        if is_prime_number(i):
            answer.append(i)
    return len(answer)

print(solution(10))
