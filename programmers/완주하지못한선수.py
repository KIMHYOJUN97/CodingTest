# def solution(participant,completion):
#     participant.sort()
#     completion.sort()

#     answer = " "
#     for i in range(len(participant)-1):
#         if participant[i] != completion[i]:
#             return participant[i]
    
#     answer = participant[-1]
#     return answer


import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[-1]

print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))