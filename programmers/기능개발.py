#스택/큐

import math

def solution(progresses, speeds):
    answer = []
    day = []
    cnt = 0
    for i in range(len(progresses)):#7 3 9
        day.append((100-progresses[i]) // speeds[i])
        if (100-progresses[i]) % speeds[i] != 0:
            day[i] += 1
            
    tmp = day[0]
    
    while day:
        if tmp >= day[0]:
            cnt += 1
            day.pop(0)
            if len(day) == 0:
                answer.append(cnt)
        else:
            answer.append(cnt)
            tmp = day[0]
            cnt = 0
            
    return answer