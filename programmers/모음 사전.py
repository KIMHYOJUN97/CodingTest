#LV2
#완전 탐색
from itertools import permutations

def solution(word):
    answer = 0
    alphabet = ['A', 'E', 'I', 'O', 'U']
    alpha = {}
    num = 0
    for i in range(5):
        tmp = alphabet[i]
        num += 1
        alpha[tmp] = num
        for j in range(5):
            tmp_j = tmp+alphabet[j]
            num += 1
            alpha[tmp_j] = num
            for k in range(5):
                tmp_k = tmp_j+alphabet[k]
                num += 1
                alpha[tmp_k] = num
                for m in range(5):
                    tmp_m = tmp_k+alphabet[m]
                    num += 1
                    alpha[tmp_m] = num
                    for n in range(5):
                        tmp_n = tmp_m+alphabet[n]
                        num += 1
                        alpha[tmp_n] = num

    answer = alpha[word]
    return answer

solution("AAAAE")