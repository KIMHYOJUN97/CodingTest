from itertools import combinations
question = list(input())

#괄호 갯수 세기
q_count = 0
for q in question:
    if q == '(':
        q_count += 1

#몇번째 괄호 없앨 것 인지 집합 형태로 만들기
#1~q_count개 까지 만들어야 함
#만약 3이라면 3개의 조합 구하기
# (0) (1) (2) 
# (0 1) (0 2) (1 2)
# (0 1 2)
dummy_list = []
for i in range(q_count):
    dummy_list.append(i)

combi_list = []
for i in range(1,q_count):
    combi_list.append(combinations(dummy_list,i))

#combi_list에 있는 숫자만 제외하고