from itertools import combinations
question = list(input())
answer = []
# test = question[:] == .copy()
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
for i in range(1,q_count+1):
    combi_list.append(list(combinations(dummy_list,i)))

print(combi_list)
#combi_list에 있는 숫자만 제외하고
for com in combi_list:
    for c in com:
        #원소의 갯수 조절하기
        tmp_question = question.copy()
        stack = []
        #순열 원소 하나씩 열거하기
        combi_one = []
        #사전형식으로 인덱스 짝 지어주기?=>안됨. (()()) 경우 인덱스가 맞지 않음.
        for _ in c:
            combi_one.append(_)
        
        answer.append(tmp_question)

#생각은 얼추 맞았으나 전개 방식에서의 문제점이 있다.
