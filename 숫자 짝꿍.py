from collections import Counter # count 함수보다 시간복잡도에서 유리함
# 시간복잡도 O(n)

def solution(X, Y):
    answer = ""
    X = Counter(X)
    Y = Counter(Y)

    for i in range(9, -1, -1): # 0~9까지 숫자 중에
        mn = min(X[str(i)], Y[str(i)]) # X, Y 에서 i가 나오는 횟수 중에 작은 횟수
        answer += str(i) * mn # i * i가 나오는 작은 횟수

    if answer == "":
        return "-1"

    if answer[0] == "0":
        return "0"

    return answer

print(solution('100', '203045'))
