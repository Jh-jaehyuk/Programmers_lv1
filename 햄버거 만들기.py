def solution(ingredient):
    answer = 0
    pack = [1, 2, 3, 1]
    i = 0
    while i <= len(ingredient)-3:
        if ingredient[i:i+4] == pack:
            answer += 1
            del ingredient[i:i+4]
            i = i-3 # i-3 까지만 돌아가면 됨. 초기화 불필요.
        else:
            i += 1
    return answer

print(solution([2,1,1,2,3,1,2,3,1]))
