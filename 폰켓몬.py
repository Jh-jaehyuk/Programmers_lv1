def solution(nums):
    if len(nums)/2 <= len(set(nums)):
        answer = int(len(nums)/2)
    else:
        answer = len(set(nums))
    return answer
#   return min(len(nums)/2, len(set(nums)))
#   답이 무조건 len(nums)/2 와 len(set(nums))) 중에 작은 값임.
print(solution([3,3,3,2,2,2]))
