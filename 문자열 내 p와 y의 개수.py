def solution(s):
    num_p = 0
    num_y = 0

    for i in s:
        if i == 'p' or i == 'P':
            num_p += 1
        elif i == 'y' or i == 'Y':
            num_y += 1

    if num_p == num_y:
        answer = True
    else:
        answer = False
# s.lower().count('p') == s.lower().count('y')
# count 함수는 문자열 안에 특정값의 개수를 세어줌.
    return answer

print(solution('pPoooyY'))

