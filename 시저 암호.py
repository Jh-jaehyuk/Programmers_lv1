from string import ascii_lowercase
from string import ascii_uppercase
from collections import deque

def solution(s, n):
    answer = []
    low = list(ascii_lowercase) # 알파벳 소문자 리스트
    up = list(ascii_uppercase) # 알파벳 대문자 리스트
    rotate_low = deque(list(ascii_lowercase))
    rotate_up = deque(list(ascii_uppercase))

    for _ in range(n):
        rotate_low.rotate(-1) # 리스트를 왼쪽으로 이동
        rotate_up.rotate(-1) # 리스트를 왼쪽으로 이동

    result = ''
    for i in range(len(s)):
        if s[i] in low:
            result += rotate_low[low.index(s[i])]
        elif s[i] in up:
            result += rotate_up[up.index(s[i])]
        else:
            result += s[i]

    answer.append(result)

    return ''.join(answer)

print(solution('DABN asdwE', 1))
