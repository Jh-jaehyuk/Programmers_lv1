def solution(price, money, count):
    i = 1
    a = 0
    while i <= count:
        a += price * i
        i += 1
    return 0 if money > a else (a - money)

print(solution(2, 20, 4))
