def solution(arr):
    # answer = []
    # i = 1
    # while i < len(arr):
    #     if arr[i-1] == arr[i]:
    #         i += 1
    #     else:
    #         answer.append(arr[i-1])
    #         i += 1
    # answer.append(arr[-1])
    # return answer

    result = []
    for c in arr:
        if len(result) == 0 or result[-1] != c:
            # 마지막에 추가한 값이 c가 아니라면 = c 가 중복되지 않으면.
            result.append(c)
    return result

print(solution([1,1,3,3,0,1,1]))


