#두 배열의 원소 교체
n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
b.sort()
for i in range(k):
    a[i] = b[n-i-1]

print(sum(a))