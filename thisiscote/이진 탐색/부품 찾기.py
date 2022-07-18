#이코테 부품 찾기

n = int(input())
thing = list(map(int,input().split()))
m = int(input())
customer = list(map(int,input().split()))

def search(thing,target):
    left = 0
    right = len(thing)-1
    while left<=right:
        mid = (left+right)//2
        if thing[mid] == target:
            return "yes"
        elif thing[mid] < target:
            left = mid+1
        else:
            right = mid-1
    
    return "no"
answer = []
for cust in customer:
    print(search(thing,cust),end=' ')
