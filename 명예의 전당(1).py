def solution(k, score):
    answer = []
    l = []
    for i in score:
        if len(l) < k:
            l.append(i)
            answer.append(min(l))
        else:
            if i >= min(l):
                l.remove(min(l))
                l.append(i)
                answer.append(min(l))
            else:
                answer.append(min(l))
    return answer

print(solution(3, [10,100,20,150,1,100,200]))
