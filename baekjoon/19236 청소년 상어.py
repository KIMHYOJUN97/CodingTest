import sys
from collections import deque
from itertools import combinations
from copy import deepcopy
input = sys.stdin.readline
#완전탐색으로 풀어야 함?
dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]
graph = []
direction_graph = []
for i in range(4):
    a,b,c,d,e,f,g,h = map(int,input().split())
    graph.append([a,c,e,g])
    direction_graph.append([b-1,d-1,f-1,h-1])
shark_direction = direction_graph[0][0]
answer_list = []
answer = graph[0][0]
graph[0][0] = -1
direction_graph[0][0] = -1
dq = deque()
dq.append([0,0])

def moving_fish(graph,direction_graph):
    visited = [0]*17
    # num_visit = 0
    while(True):
        target_index = []
        # flag = 0
        min_num = 17
        for i in range(4):
            for j in range(4):
                if visited[graph[i][j]]==0 and graph[i][j] != -1 and graph[i][j]<min_num:
                    target_index = [i,j]
                    min_num = graph[i][j]
        if len(target_index)==0:
            break
        visited[graph[target_index[0]][target_index[1]]]=1
        
        # cnt_visit = 0
        # for i in range(17):
        #     if visited[i]==1:
        #         cnt_visit+=1
        # if(cnt_visit==num_visit):
        #     break
        # num_visit = cnt_visit           
        while(True):
            nx = target_index[1]+dx[direction_graph[target_index[0]][target_index[1]]]
            ny = target_index[0]+dy[direction_graph[target_index[0]][target_index[1]]]
            if nx >=0 and ny>=0 and nx <4 and ny<4 and graph[ny][nx]!=-1:
                graph[target_index[0]][target_index[1]],graph[ny][nx] = graph[ny][nx],graph[target_index[0]][target_index[1]]
                direction_graph[target_index[0]][target_index[1]],direction_graph[ny][nx] = direction_graph[ny][nx],direction_graph[target_index[0]][target_index[1]]
                break
            else:
                direction_graph[target_index[0]][target_index[1]] = (direction_graph[target_index[0]][target_index[1]]+1)%8
                
#각 칸을 지날때마다 갈수있는 칸을 조합으로 나열해서
#계속 넣는다
def find_fish(position,graph,direction):
    fish_list = []
    while(True):
        nx = position[1]+dx[direction]
        ny = position[0]+dy[direction]
        if nx>=0 and ny>=0 and nx<4 and ny<4 and graph[ny][nx]!=0:
            fish_list.append([ny,nx])
            position = [ny,nx]
        else:
            break

    return fish_list
shark_position = [0,0]
def moving_shark(graph,direction):
    moving_fish(graph,direction_graph)
    fish = find_fish(shark_position,graph,shark_direction)
    
    

