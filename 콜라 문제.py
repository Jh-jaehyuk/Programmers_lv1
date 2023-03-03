def solution(a, b, n):
    answer = 0
    while n >= a:
        submit_bottle = n//a * a # 제출한 병 수
        return_bottle = n//a * b # 받은 콜라 수
        extra_bottle = n - submit_bottle # 남은 병 수
        n = extra_bottle + return_bottle
        answer += return_bottle
    return answer
# 문제를 잘 읽고 변수 설정을 영리하게 할 것.

print(solution(3,1,20))
