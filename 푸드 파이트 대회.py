import math
def solution(food):
    s = []
    for i in range(1, len(food)):
        s.append(str(i) * int(math.floor(food[i]/2)))
    return ''.join(s) + '0' + ''.join(s[::-1])

print(solution([1,7,1,2]))
