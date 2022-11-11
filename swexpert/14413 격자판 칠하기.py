T = int(input())
dy = [-1,1,0,0]
dx = [0,0,-1,1]

def check_graph(graph,y,x,n,m):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if(nx >=0 and ny>=0 and nx <m and ny<n):
            if(graph[y][x]=='#'):
                if graph[ny][nx] =='#':
                    return 1
                else:
                    graph[ny][nx]='.'
            if(graph[y][x]=='.'):
                if graph[ny][nx]=='.':
                    return 1
                else:
                    graph[ny][nx]='#'
        
    return 0

for t in range(1,T+1):
    flag = 0
    n,m =map(int,input().split())
    graph =[]
    for i in range(n):
        graph.append(list(input()))
    for i in range(n):
        for j in range(m):
            if(check_graph(graph,i,j,n,m)==1):
                flag = 1
                break
        if flag==1:
            print("#{} {}".format(t,"impossible"))
            break
    if(flag==0):
        print("#{} {}".format(t,"possible"))