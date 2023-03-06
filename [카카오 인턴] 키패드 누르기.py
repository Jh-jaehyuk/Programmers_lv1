def solution(numbers, hand):
    answer = ''
    r_cood = [0,0] # 처음 오른손 위치
    l_cood = [2,0] # 처음 왼손 위치
    num_cood = [[1,0], [0,3], [1,3], [2,3], [0,2], [1,2],
                [2,2], [0,1], [1,1], [2,1]]
    # 숫자 패드를 좌표로 변환하여 리스트로 저장

    for i in numbers:
        print('i = ', i)
        print('l_cood = ', l_cood)
        print('r_cood = ', r_cood)
        if i == 1 or i == 4 or i == 7:
            l_cood = num_cood[i]
            answer += 'L'
        elif i == 3 or i == 6 or i == 9:
            r_cood = num_cood[i]
            answer += 'R'
        else:
            if abs(l_cood[0]-num_cood[i][0]) + abs(l_cood[1]-num_cood[i][1]) < abs(r_cood[0]-num_cood[i][0]) + abs(r_cood[1]-num_cood[i][1]):
                l_cood = num_cood[i]
                answer += 'L'
            elif abs(l_cood[0]-num_cood[i][0]) + abs(l_cood[1]-num_cood[i][1]) > abs(r_cood[0]-num_cood[i][0]) + abs(r_cood[1]-num_cood[i][1]) :
                 r_cood = num_cood[i]
                 answer += 'R'
            elif abs(l_cood[0]-num_cood[i][0]) + abs(l_cood[1]-num_cood[i][1]) == abs(r_cood[0]-num_cood[i][0]) + abs(r_cood[1]-num_cood[i][1]):
                if hand == 'right':
                    r_cood = num_cood[i]
                    answer += 'R'
                else:
                    l_cood = num_cood[i]
                    answer += 'L'

    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))
