def solution(answers):
    answer1 = [1,2,3,4,5] * int(len(answers)//5 + 1)
    answer2 = [2,1,2,3,2,4,2,5] * int(len(answers)//8 + 1)
    answer3 = [3,3,1,1,2,2,4,4,5,5] * int(len(answers)//10 + 1)
    score1 = 0
    score2 = 0
    score3 = 0
    answer = []

    for i in range(len(answers)):
        if answers[i] == answer1[i]:
            score1 += 1

        if answers[i] == answer2[i]:
            score2 += 1

        if answers[i] == answer3[i]:
            score3 += 1
    l = []
    l.append(score1)
    l.append(score2)
    l.append(score3)
    for i in range(len(l)):
        if l[i] == max(l):
            answer.append(i+1)

    return list(sorted(answer))

print(solution([1,3,2,4,2]))
