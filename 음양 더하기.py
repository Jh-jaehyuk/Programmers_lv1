def solution(absolutes, signs):
    # l = []
    # for i in range(len(absolutes)):
    #     if signs[i] == True:
    #         l.append(absolutes[i])
    #     else:
    #         l.append(absolutes[i] * -1)
    # answer = sum(l)
    # return answer
    
    answer = 0
    for absolute, sign in zip(absolutes, signs):
    # zip 은 두가지 리스트를 튜플로 짝지어줌. ex) [(absolute, sign)]
        if sign:
            answer += absolute
        else:
            answer -= absolute
    return answer
