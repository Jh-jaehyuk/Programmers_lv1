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

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if len(get_divisor(i)) % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer


# def solution(left, right):
#     answer = 0
#     for i in range(left,right+1):
#         if int(i**0.5)==i**0.5: 제곱수라면 제곱근도 자연수임.
#             answer -= i
#         else:
#             answer += i
#     return answer
# 약수의 개수가 홀수인 수는 모두 제곱수임을 이용한 풀이.

print(solution(24, 27))

