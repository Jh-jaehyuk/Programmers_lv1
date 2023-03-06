def solution(babbling):
    answer = 0
    speak_list = ['aya', 'ye', 'woo', 'ma']
    for i in babbling:
        for j in speak_list:
            if j*2 not in i:
                i = i.replace(j, ' ')
        if i.strip() == '': # 공백을 제거하고 '' 이면
            answer += 1
    return answer

print(solution(['woayao']))
