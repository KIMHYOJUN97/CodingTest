#바깥에 있는 경우
#안쪽에 있는 경우 두가지를 나눠서 체크한다.
#완전탐색을 해야할까?=>조합이용?=>시간초과
# from itertools import combinations

# n = int(input())
# circle = []
# answer = "YES"
# for i in range(n):
#     circle.append(list(map(int,input().split())))
# circle_combinations = list(combinations(circle,2))
# for com in circle_combinations:
#     d = abs(com[0][0]-com[1][0])
#     plus = com[0][1]+com[1][1]
#     minus = abs(com[0][1]-com[1][1])
#     if minus <d <plus:
#         answer = "NO"
#         break
#     elif plus == d:
#         answer = "NO"
#         break
#     elif minus == d:
#         answer = "NO"
#         break
#     else:
#         continue

# print(answer)

#스택이용
#(x-r):여는 기호 (x+r) 닫는기호로 생각
#현재가 open 다음이 다른원의 close일 경우 NO 반환

n = int(input())
circles = []
open = 0
close = 1

for i in range(n):
    x,r = map(int,input().split())
    circles.append([x-r,open,i])
    circles.append([x+r,close,i])

circles.sort(key = lambda x:x[0])
print(circles)
stack = []
attached = set()
for circle in circles:
    if circle[0] in attached:
        print("NO")
        exit(0)
    if circle[1] == open:
        stack.append(circle)
        attached.add(circle[0])
    elif stack[-1][2] != circle[2]:
        print("NO")
        exit(0)
    else:
        attached.add(circle[0])
        stack.pop()
print("YES")