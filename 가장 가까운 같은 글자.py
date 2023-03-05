def solution(s):
    answer = []
    d = dict()

    for idx, word in enumerate(list(s)):
        if word not in d:
            answer.append(-1)
            d[word] = idx
        else:
            answer.append(idx - d[word])
            d[word] = idx

    return answer

print(solution('banana'))
print(list(enumerate('banana')))
