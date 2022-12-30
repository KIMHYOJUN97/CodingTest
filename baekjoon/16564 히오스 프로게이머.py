#binary_search
#mid값이 대부분 문제에서 원하는 값일 확률이 높다
#mid는 대부분 최대 or 최소이다
#start,end의 값 설정 방법은 mid가 나타내는 값이 무엇일지 잘 생각해보자.

import sys
input = sys.stdin.readline

N,K = map(int,input().split())
char_list = []
for i in range(N):
    char_list.append(int(input()))

start = min(char_list)
end = min(char_list)+K
answer =0
while start<=end:
    mid = (start+end)//2 #목표값

    sum = 0
    for char in char_list:
        if mid>char:
            sum += mid-char
    
    if sum<=K:
        answer = max(answer,mid)
        start = mid+1
    else:
        end = mid - 1
print(answer)