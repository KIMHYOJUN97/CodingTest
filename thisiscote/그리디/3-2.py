#큰 수의 법칙
#내 풀이

n,m,k = map(int,input().split())
lst = list(map(int,input().split()))
count = 0

lst.sort()

for i in range(m):
    if(i % k == 0) and i != 0:
        count += lst[-2]
    else:
        count += lst[-1]

print(count)

#책 풀이
n,m,k = map(int,input().split())
data = list(map(int,input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)

#수열 공식 이용하여 가장 독창적이라 생각!

n,m,k = map(int,input().split())
data = list(map(int,input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

count = int(m/(k+1))*k
count += m%(k+1)

result = 0
result += (count) * first
result += (m-count) * second

print(result)
