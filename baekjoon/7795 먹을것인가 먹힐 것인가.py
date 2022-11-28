import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n,m = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    answer = 0
    A.sort(reverse=True)
    B.sort()
    for a in A:
        for b in B:
            if a>b:
                answer+=1
            else:
                break

    print(answer)