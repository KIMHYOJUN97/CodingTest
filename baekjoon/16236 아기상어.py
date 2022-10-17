import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

shark_position = []
for i in range(n):
    for j in range(n):
        if graph[i][j]==9:
            shark_position =[i,j]
            break
    if(shark_position):
        break

def find_fish(s_size):
    fish_list = []
    for i in range(n):
        for j in range(n):
            if (0<graph[i][j]<s_size):
                fish_list.append([i,j])
    
    return fish_list
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def moving_shark(fish,shark_size):
    graph_copy = [[0]*n for i in range(n)]
    visited = [[0]*n for i in range(n)]
    visited[shark_position[0]][shark_position[1]]=1
    dq = deque()
    dq.append([shark_position[0],shark_position[1]])
    #fish의 위치는 리스트 형태로 들어올 수도 있다.
    #하지만 fish값은 고정으로 1개의 위치만 들어오고
    #같은 크기의 fish가 많다면 대소비교를 통해 보여준다.
    graph_copy[fish[0]][fish[1]]=-1
    while dq:
        now = dq.popleft()
        for i in range(4):
            nx = now[1] + dx[i]
            ny = now[0] + dy[i]
            if nx >=0 and nx<n and ny>=0 and ny<n and graph[ny][nx]<=shark_size and visited[ny][nx]==0:
                visited[ny][nx]=1
                graph_copy[ny][nx]= graph_copy[now[0]][now[1]]+1
                dq.append([ny,nx])
    return graph_copy[fish[0]][fish[1]]

shark_size = 2
answer = 0
eated_fish = 0

dq = deque()
dq.append(find_fish(shark_size))
graph[shark_position[0]][shark_position[1]]=0
while dq:
    fish_list = dq.popleft()
    if len(fish_list)==0:
        break
    min_reach = 400
    #이동거리가 가장 짧은 구간 찾기
    for fish in fish_list:
        if (moving_shark(fish,shark_size) != -1 and moving_shark(fish,shark_size)<min_reach):
            min_reach = moving_shark(fish,shark_size)

    selected_fish = []
    for fish in fish_list:
        if(moving_shark(fish,shark_size)==min_reach):
            selected_fish.append(fish)

    min_fish_y = 21
    go_fish = []
    for fish in selected_fish:
        if fish[0]<min_fish_y:
            min_fish_y = fish[0]
    for fish in selected_fish:
        if fish[0]==min_fish_y:
            go_fish.append(fish)

    min_fish_x = 21
    real_fish = []
    for go in go_fish:
        if go[1]<min_fish_x:
            min_fish_x = go[1]
            real_fish = go

    if len(real_fish)==0 or moving_shark(real_fish,shark_size)==-1:
        break
    answer+=moving_shark(real_fish,shark_size)
    graph[real_fish[0]][real_fish[1]]=0
    eated_fish+=1
    if(eated_fish == shark_size):
        eated_fish =0
        shark_size +=1
    shark_position=real_fish
    dq.append(find_fish(shark_size))
print(answer)