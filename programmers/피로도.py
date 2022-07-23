#완전탐색
#LV2
from itertools import permutations

def solution(k, dungeons):
    all_dun = list(permutations(dungeons))
    answer_list = []
    for dun in all_dun:
        new_k = k
        new_answer = 0
        for d in dun:
            if new_k >= d[0]:
                new_k -= d[1]
                new_answer += 1
        answer_list.append(new_answer)
    
    return max(answer_list)