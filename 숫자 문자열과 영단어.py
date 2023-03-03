def solution(s):
    for num, eng in enumerate(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
        if eng in s:
            s = s.replace(eng, str(num))
    answer = int(s)
    return answer

print(solution("23four5six7"))
