import sys
input = sys.stdin.readline

T = int(input())
dp = [0]*100001
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 2
dp[4] = 3
for i in range(5,100001):
    if(i>=6):
        dp[i] = dp[i-2]+dp[i-4]+dp[i-6]
    else:
        dp[i] = dp[i-2]+dp[i-4]

for _ in range(T):
    n = int(input())
    print(dp[n]%1000000009)