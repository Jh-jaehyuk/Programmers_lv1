import string
def solution(s, skip, index):
    l = list(i for i in string.ascii_lowercase if i not in skip)*3
    new_s = []
    for i in s:
        new_s.append(l[l.index(i)+index])
    answer = ''.join(new_s)
    return answer

print(solution('aukks','wbqd',5))
