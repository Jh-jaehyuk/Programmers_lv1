def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)

def solution(n, m):
    answer = [gcd(n, m), (n/gcd(n, m) * m)]
    return answer

print(solution(2, 5))
