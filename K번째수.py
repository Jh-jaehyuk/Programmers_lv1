def solution(array, commands):
    return [sorted(array[commands[i][0]-1:commands[i][1]])[commands[i][2]-1] for i in range(len(commands))]
#   return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
#   map, lambda를 이용하는 방법도 있음. 조금 더 간결해서 가독성이 좋음.

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
