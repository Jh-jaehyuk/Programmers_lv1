def solution(s):
    answer = []
    l = s.split(' ')

    for i in range(len(l)):
        result = ''
        for j in range(len(l[i])):
            if j % 2 == 0:
                result += l[i][j].upper()
            else:
                result += l[i][j].lower()

        answer.append(result)

    return ' '.join(answer)

print(solution('try hello world'))

