def solution(strings, n):
    return sorted(strings, key=lambda x:(x[n], x))
# x[n]으로 먼저 정렬하고 x 자체를 비교해서 사전순으로 정렬
print(solution(["abce", "abcd", "cdx"], 2))
