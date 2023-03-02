def ten_to_n(n, q):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)
    return rev_base

def solution(n):
    a = ten_to_n(n, 3)
    answer = int(str(a), 3)
    return answer

# def solution(n):
#     tmp = ''
#     while n:
#         tmp += str(n % 3) # 3진수로 만드는 과정
#         n = n // 3
#
#     answer = int(tmp, 3) # 3진수를 10진수로 변환환#     return answer

print(solution(45))
