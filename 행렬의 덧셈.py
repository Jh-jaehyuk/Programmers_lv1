import numpy as np
def solution(arr1, arr2):
    np_arr1 = np.array(arr1)
    np_arr2 = np.array(arr2)
    return (np_arr1 + np_arr2).tolist()

def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a,b)] for a, b in zip(A,B)]
    return answer

# zip으로 행렬 두개를 짝지어준 다음 각각의 요소 합을 리스트로 구성함.
# 짧고 간결하게 좋은 코드인 것 같음.
# 주어진 값이 리스트 2개일 경우엔 꼭 zip 함수를 기억하자!

print(solution([[1,2], [2,3]], [[3,4], [5,6]]))
