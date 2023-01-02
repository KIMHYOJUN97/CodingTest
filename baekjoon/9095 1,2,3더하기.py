from sys import stdin
input = stdin.readline

T = int(input())
dp=[1,1,2,4,7,13]
for i in range(6,11):
    dp.append(dp[i-2]+2*dp[i-3]+3*dp[i-4]+2*dp[i-5]+dp[i-6])

for _ in range(T):
    print(dp[int(input())])