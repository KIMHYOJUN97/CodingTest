#계수 정렬
#숫자의 범위가 적을 때 가장 효과적으로 사용 O(N+K)

array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
count = [0] *(max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i,end = ' ')