def solution(num):
    answer = ''.join("Even" if num%2 == 0 else "Odd")
    # if num%2 == 0:
    #     answer = "Even"
    # else:
    #     answer = "Odd"

    return answer

print(solution(4))
