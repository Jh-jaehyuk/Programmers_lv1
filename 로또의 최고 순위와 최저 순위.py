def solution(lottos, win_nums):
    count = 0
    zero_count = lottos.count(0)
    grade = [6,6,5,4,3,2,1]
    for i in lottos:
        if i in win_nums:
            count += 1

    answer = [grade[count+zero_count], grade[count]]
    return answer

print(solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]))
