# def solution(d, budget):
#     length = len(d)
#     min_d = min(d)
#     count = 0
#     while budget - min_d >= 0:
#         count += 1
#         if count == length:
#             return count
#         else:
#             d.remove(min_d)
#             budget -= min_d
#             min_d = min(d)
#
#     return count

def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)
# d를 오름차순으로 정렬하고 pop으로 제일 큰 값 먼저 제거함.

print(solution([2,2,3,3], 10))
