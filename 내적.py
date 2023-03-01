def solution(a, b):
    # return sum([a[i]*b[i] for i in range(len(a))])
    return sum([x*y for x, y in zip(a, b)])
    # 리스트 두개가 변수로 나오는 경우 zip 함수 이용하면 편리할 수도 있음.

print(solution([-1,0,1],[1,0,-1]))
