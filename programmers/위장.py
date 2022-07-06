#조합으로 풀어볼까?
#총 cloth개수 + 종류별개수*종류
#dict의 크기 구하는 메서드
def solution(clothes):
    answer = 1

    dict = {}
    for cloth in clothes:
        key = cloth[1]
        value = cloth[0]
        if key in dict:
            dict[key].append(value)
        else:
            dict[key] =[value]
    
    for key in dict.keys():
        result = result*(len(dict[key])+1)
        
    return result-1