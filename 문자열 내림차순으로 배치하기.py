def solution(s):
    return ''.join(sorted(s, reverse=True))
# 알파벳, 한글도 sorted 로 정렬 가능함을 기억할 것.
# a -> z 순으로 정렬. reverse 할 시엔 z -> a 순으로 정렬.
print(solution('ansaiASad'))
