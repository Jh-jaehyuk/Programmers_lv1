def solution(N, stages):
    stages.sort()
    fail = []
    answer = []
    l = [i for i in range(1, N+2)]
    for i in range(len(l)):
        l[i] = stages.count(i+1)

    for i in range(len(l)-1):
        if l[i:] == 0:
            fail.append(0)
        else:
            fail.append((l[i]/sum(l[i:])))

    fail = list(enumerate(fail, start=1))
    fail = sorted(fail, key=lambda x: (x[1]), reverse=True)

    for i in range(len(fail)):
        answer.append(fail[i][0])

    return answer

print(solution(5, [2,1,2,6,2,4,3,3]))

# def solution(N, stages): # 나중에 다시 확인해보기.
#     answer = []
#     fail = []
#     info = [0] * (N + 2)
#     for stage in stages:
#         info[stage] += 1
#     for i in range(N):
#         be = sum(info[(i + 1):])
#         yet = info[i + 1]
#         if be == 0:
#             fail.append((str(i + 1), 0))
#         else:
#             fail.append((str(i + 1), yet / be))
#     for item in sorted(fail, key=lambda x: x[1], reverse=True):
#         answer.append(int(item[0]))
#     return answer



