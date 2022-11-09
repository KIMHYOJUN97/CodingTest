from collections import defaultdict

t = int(input())
for i in range(1,t+1):
    max = 0
    cnt = 0
    n = int(input())
    score = list(map(int,input().split()))
    score_dict = defaultdict(int)
    for s in score:
        score_dict[s]+=1
    for j in range(101):
        if(score_dict[j]>=cnt):
            cnt = score_dict[j]
            max = j
    
    print("#{} {}".format(i,max))