def solution(n):
    # l = ['수', '박']
    # if n % 2 == 0:
    #     return ''.join(l) * int(n/2)
    # else:
    #     return ''.join(l) * int((n-1)/2) + l[0]

    l = '수박' * n
    return l[:n]
    # 문자가 반복되는 규칙을 이용한 풀이. 짧고 간결함

print(solution(6))
print(solution(5))
