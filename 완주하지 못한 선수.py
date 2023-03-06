from collections import Counter
# 카운터끼리 연산이 가능하므로 겹치는 값을 제외하고 싶을 때 유용함
# + 시간복잡도 이득!
def solution(participant, completion):
    p_counter = Counter(participant)
    c_counter = Counter(completion)
    answer = p_counter - c_counter
    return list(answer.keys())[0]

print(solution(['leo', 'kiki', 'eden'], ['eden', 'kiki']))
