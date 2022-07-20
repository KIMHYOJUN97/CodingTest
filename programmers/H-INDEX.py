#정렬
#LV2

def solution(citations):
    #0 1 3 5 6
    #10 10 10 10 10 ->5?
    citations.sort()
    answer = len(citations)
    while answer !=0:
        more =0
        less = 0
        for ci in citations:
            if ci >=answer:
                more+=1
            if ci <= answer:
                less += 1
        if less <= answer <= more:
            return answer
        else:
            answer -= 1

    return answer
