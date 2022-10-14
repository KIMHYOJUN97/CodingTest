import sys
input = sys.stdin.readline

dx = [0,-1,-1,0,1,1,1,0,-1]#첫 번째 값은 더미
dy = [0,0,-1,-1,-1,0,1,1,1]
n,m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))
direction = []
for i in range(m):
    a,b = map(int,input().split())
    direction.append((a,b))
cloud = [[n-2,0],[n-1,0],[n-1,1],[n-2,1]]
def find_cross(graph,cloud):
    dc_x=[-1,-1,1,1]
    dc_y=[-1,1,-1,1]
    for i in range(len(cloud)):
        cnt = 0
        for j in range(4):
            nx = cloud[i][1]+dc_x[j]
            ny = cloud[i][0]+dc_y[j]
            if(nx>=0 and nx<n and ny>=0 and ny <n and graph[ny][nx]!=0):
                cnt+=1
        graph[cloud[i][0]][cloud[i][1]]+=cnt

# def make_cloud(graph,cloud):
#     new_cloud = []
#     for i in range(n):
#         for j in range(n):
#             flag = 0
#             for k in range(len(cloud)):
#                 if(cloud[k][0]==i and cloud[k][1]==j):
#                     flag = 1
#                     break
#             if flag==1 or graph[i][j] < 2:
#                 continue    
#             new_cloud.append([i,j])
#     return new_cloud

def make_cloud(graph,cloud):
    visited = [[0]*n for i in range(n)]
    new_cloud = []
    for c in cloud:
        visited[c[0]][c[1]]=1
    for i in range(n):
        for j in range(n):
            if(graph[i][j]>=2 and visited[i][j]==0):    
                new_cloud.append([i,j])
    
    return new_cloud

for d,c in direction:
    for i in range(len(cloud)):
        cloud[i][0] += dy[d]*c
        cloud[i][1] += dx[d]*c
        if(cloud[i][0] >=n):
            cloud[i][0]%=n
        elif(cloud[i][0] <0):
            while(cloud[i][0]<0):
                cloud[i][0]+=n
        if(cloud[i][1] >=n):
            cloud[i][1] %=n
        elif(cloud[i][1]<0):
            while(cloud[i][1]<0):
                cloud[i][1]+=n
        graph[cloud[i][0]][cloud[i][1]]+=1
    find_cross(graph,cloud)
    cloud = make_cloud(graph,cloud)
    for c in cloud:
        graph[c[0]][c[1]] -= 2

water = 0
for i in range(n):
    for j in range(n):
        water += graph[i][j]
print(water)