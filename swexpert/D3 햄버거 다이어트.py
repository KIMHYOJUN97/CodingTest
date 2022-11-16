T = int(input())

def dfs(score, kcal,idx):
    if kcal >target:
        return
    score_list.append(score)
    if idx==n:
        return
    s = score + menu[idx][0]
    k = kcal + menu[idx][1]

    dfs(s,k,idx+1)
    dfs(score,kcal,idx+1)

for t in range(1,T+1):
    n,target = map(int,input().split())
    menu = []
    score_list = []
    for i in range(n):
        menu.append(list(map(int,input().split())))
    dfs(0,0,0)
    print("#{} {}".format(t,max(score_list)))