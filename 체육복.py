def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    l = [i for i in lost]

    for i in l:
        if i in reserve:
            lost.remove(i)
            reserve.remove(i)

    l = [i for i in lost]

    for i in lost:
        if (i-1) in reserve:
            if i in l:
                l.remove(i)
                reserve.remove(i-1)
            else:
                reserve.remove(i-1)

        elif (i+1) in reserve:
            if i in l:
                l.remove(i)
                reserve.remove(i+1)
            else:
                reserve.remove(i+1)
    print(l)
    return n - len(l)

# 반복문 안에서 remove 할 경우 원본 리스트가 지워지면서 예상과 다르게 답이 나옴.
# 반목문 안에서 remove 해야할 경우 원본을 복제한 리스트로 진행할 것.

print(solution(5,[1,2,4],[2,3,4,5]))
