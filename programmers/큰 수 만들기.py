#큰 수 만들기
#LV2

#dictionary도 정렬이 되는가?
#순열:중복없고 순서대로

from itertools import combinations

def solution(number, k):
    num = list((number))
    r = len(number)-k
    num_list = list(combinations(num,r))
    lst = []
    for i in num_list:
        tmp = ''
        for j in range(len(i)):
            tmp += i[j]
        lst.append(int(tmp))

    return str(max(lst))

#처음 내 식 간단하게
def solution(number, k):
    answer = list(combinations(list(number), len(number)-k))
    return ''.join(sorted(answer, reverse = True)[0])

#스택의 마지막값이 다음에 들어올 수보다 작으면 다음에 들어올 수보다 크거나,
#같을 때 까지 pop해준다.
def solution(number, k):
    answer = [] # Stack
    
    for num in number:
        if not answer:
            answer.append(num)
            continue
        if k > 0:
            while answer[-1] < num:
                answer.pop()
                k -= 1
                if not answer or k <= 0:
                    break
        answer.append(num)
        
    answer = answer[:-k] if k > 0 else answer
    return ''.join(answer)#list각각을 더해주는 메서드

def solution(number, k):
    answer = [] # Stack
    
    for num in number:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)
        
    return ''.join(answer[:len(answer) - k])
