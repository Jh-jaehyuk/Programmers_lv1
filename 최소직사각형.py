def solution(sizes):
    l = max([min(i) for i in sizes])
    m = max([max(i) for i in sizes])
    answer = l * m
    return answer

# 문제 해결의 아이디어가 중요한 문제! 기발한 생각이 필요하다.
# 모든 명함들의 긴 모서리를 가로로 돌려서 겹쳐봅시다.
# 그 상태에서 지갑에 한번에 넣을 수 있으려면 세로길이는 어떻게 해야할지 상상해봅시다!
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))
