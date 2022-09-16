#시간 초과

# n = int(input())
# top = list(map(int,input().split()))
# answer = []
# for idx,t in enumerate(top):
#     cnt = idx-1
#     flag = 0
#     while cnt >=0:
#         if top[cnt] > t:
#             answer.append(cnt+1)
#             flag = 1
#             break
#         else:
#             cnt -= 1
#     if flag == 0:
#         answer.append(0)
# for a in answer:
#     print(a,end = ' ')
N = int(input())  # 탑의 개수
top_list = list(map(int, input().split()))  # 탑 리스트
stack = []
answer = []

for i in range(N):
    while stack:
        if stack[-1][1] > top_list[i]:  # 수신 가능한 상황
            answer.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    if not stack:  # 스택이 비면 레이저를 수신할 탑이 없다.
        answer.append(0)
    stack.append([i, top_list[i]])  # 인덱스, 값

print(" ".join(map(str, answer)))

#왼쪽으로 볼 때 오른쪽에 있는것보다 큰 건물들만 남으면
#레이저를 전부 캐치할 수 있음.