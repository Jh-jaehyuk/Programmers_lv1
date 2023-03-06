import math
def solution(k, m, score):
    answer = 0
    score = list(sorted(score, reverse=True))
    l = []
    for i in range(math.ceil(len(score)/m)):
        if len(score) >= m:
            l.append(score[i*m:(i+1)*m])
        else:
            return 0

    for i in l:
        if len(i) == m:
            answer += min(i) * m
        else:
            pass
    return answer

# def solution(k, m, score):
#     answer = 0
#     score.sort(reverse=True)
#     apple_box = []
#     for i in range(0, len(score), m): # m 간격만큼 띄고 반복문
#         apple_box.append(score[i:i+m])
#     for apple in apple_box:
#         if len(apple) == m:
#             answer += min(apple) * m
#
#     return answer
