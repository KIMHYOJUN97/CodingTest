#탐욕법 LV1
#전처리과정이 필요->reserve한 학생도 lost할 수 있다.
def solution(n, lost, reserve):
    set_reserve = set(reserve)-set(lost)
    set_lost = set(lost)-set(reserve)
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    return n-len(set_lost)

n, lost, reserve = (
        30,
        [18, 21 ], # 16개
        [ 3, 4, 5, 6, 8,13,17, 22, 23, 26,28], # 25개
    )

# def solution(n, lost, reserve):
    
#     same =[]
#     for l in lost:
#         for r in reserve:
#             if l == r:
#                 same.append(l)
#     for i in range(len(same)):
#         lost.remove(same[i])
#         reserve.remove(same[i])
#     lost_plus = [i+1 for i in lost]
#     lost_minus = [i-1 for i in lost]
#     comp1 = list(set(lost_plus)-set(reserve))
#     comp2 = list(set(lost_minus)-set(reserve))
    
#     comp3 = set(comp1)|set(comp2)
            
#     # all=set(lost_plus)+set(lost_plus)-set(reserve) #모든 경우의 수
#     answer = min(len(comp1),len(comp2))
#     if comp1 and comp2:
#         if not list(set(reserve)-comp3):
#             answer =0
#     return n-answer