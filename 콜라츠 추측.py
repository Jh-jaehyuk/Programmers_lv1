def solution(num):
    count = 0
    while num != 1:
        if num % 2 == 0:
            num /= 2
            count += 1
        elif num % 2 == 1:
            num *= 3
            num += 1
            count += 1
        if count >= 500: # num과 다른 조건이기에 별도의 if에 작성
            return -1
    return count

print(solution(626331))
