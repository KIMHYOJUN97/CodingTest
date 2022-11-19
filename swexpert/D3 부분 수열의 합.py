#분할 정복?=>조합으로 풀어도 풀리긴 한다.

T = int(input())

def dfs(N,sum):
    global answer
    if k < sum:
        return 
    #뿌리의 끝까지 내려감.
    if n==N:
        if sum==k:
            answer+=1
        return
    
    #다음 수를 더한다고 선택한 가지
    dfs(N+1,sum+arr[N])
    #다음 수를 더하지 않는다고 선택한 가지
    dfs(N+1,sum)

for t in range(1,T+1):
    n,k=map(int,input().split())
    arr = sorted(list(map(int,input().split())))
    answer = 0 
    dfs(0,0)
    print("#{} {}".format(t,answer))
