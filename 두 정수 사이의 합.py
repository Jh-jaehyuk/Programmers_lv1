def solution(a, b):
    # if a == b:
    #     return a
    # elif a > b:
    #     return sum([i for i in range(b, a+1)])
    # elif a < b:
    #     return sum([i for i in range(a, b+1)])
    return sum(range(min(a,b), max(a,b)+1))
# min, max를 이용하면 한줄로 정리가능
print(solution(3, 3))
print([i for i in range(3, 6)])
