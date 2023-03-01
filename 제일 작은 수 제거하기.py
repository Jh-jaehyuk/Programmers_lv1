def solution(arr):
    arr.remove(min(arr))
    answer = [i for i in arr]
    return answer if len(arr) != 0 else [-1]

print(solution([4,3,2,1]))
