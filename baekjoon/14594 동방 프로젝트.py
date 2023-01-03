from sys import stdin
input = stdin.readline

N = int(input())
M = int(input())
board = []
for i in range(1,N+1):
    board.append(i)
for _ in range(M):
    x,y = map(int,input().split())
    min_number = min(board[x-1:y])
    for i in range(x-1,y):
        board[i]=min_number
cnt = 0
for i in range(N):
    if board[i]==(i+1):
        cnt+=1
print(cnt)