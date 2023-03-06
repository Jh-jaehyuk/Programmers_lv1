def get_divisor(n): # n의 약수를 구하는 함수
    divisors = []
    length = int(n**0.5) + 1
    if n == 1:
        divisors = [1]
    else:
        for i in range(1, length):
            if n % i == 0:
                if i == n//i: # 제곱수에서 나오는 중복된 경우 제거
                    divisors.append(i)
                else:
                    divisors.append(i)
                    divisors.append(n//i)

    divisors.sort()
    return divisors

def solution(number, limit, power):
    answer = []
    for i in range(1, number+1):
        if len(get_divisor(i)) > limit:
            answer.append(power)
        else:
            answer.append(len(get_divisor(i)))
    return sum(answer)
