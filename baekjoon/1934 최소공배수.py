import sys
input = sys.stdin.readline

def gcd(a,b):
    if(b==0): return a
    else:
        return gcd(b,a%b)


T = int(input())
for t in range(T):
    a,b = map(int,input().split())
    print(a*b//gcd(a,b))
