def solution(cards1, cards2, goal):
    a = 0
    b = 0
    for i in goal:
        if cards1[a] == i:
            a += 1
            if a > len(cards1)-1:
                a = len(cards1)-1
        elif cards2[b] == i:
            b += 1
            if b > len(cards2)-1:
                b = len(cards2)-1
        else:
            return 'No'
    answer = 'Yes'
    return answer

print(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]))
