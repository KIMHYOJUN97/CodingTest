#heap LV3
import heapq

def solution(operations):
    answer = []
    data =[]
    for i in range(len(operations)):
        input_data = operations[i].split()
        data.append([input_data[0],int(input_data[1])])
    
    for d in data:
        if d[0] == 'I':
            answer.append(d[1])
        elif answer and d[0] == 'D':
            if d[1] == 1:
                answer.sort()
                answer.remove(answer[-1])
            else:
                answer.sort()
                answer.remove(answer[0])
    if not answer:
        return [0,0]
    else:
        answer.sort()
        return [answer[-1],answer[0]]