def solution(a, b):
    day_list = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    num_list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = 0
    for i in range(0, a-1):
        day += num_list[i]
    day += b-1
    day %= 7
    answer = day_list[day]
    return answer
# 주어진 날짜가 1월 1일부터 며칠 뒤인지를 구하고 그 날짜를 7로 나누어
# 남은 나머지를 금요일로부터 더해준다.

print(solution(5, 24))
