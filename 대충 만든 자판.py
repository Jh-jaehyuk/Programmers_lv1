def solution(keymap, targets):
    idx = []
    min_key = []
    answer = []
    for i in range(len(targets)):
        for j in targets[i]:
            for k in keymap:
                if j in k:
                    idx.append(k.index(j))
            if len(idx) == 0:
                min_key = [-1]
                break
            min_key.append(min(idx)+1)
            idx = []
        answer.append(sum(min_key))
        min_key = []

    return answer

print(solution(['ABCE'], ['ABDE']))
