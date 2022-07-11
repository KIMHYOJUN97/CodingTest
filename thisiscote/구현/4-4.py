#게임 개발
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

n,m = map(int,input().split())
d = [[0]*m for i in range(n)] #방문 여부
p_x,p_y,direction = map(int,input().split())
d[p_x][p_y] = 1
dx = [-1,0,1,0]
dy = [0,1,0,-1]

array =[]
for i in range(n):
    array.append(list(map(int,input().split())))

count = 1
turn_time = 0
while True:
    turn_left()
    nx = p_x + dx[direction]
    ny = p_y + dy[direction]
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] =1
        p_x = nx
        p_y = ny 
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    
    if turn_time == 4:
        nx = p_x - dx[direction]
        ny = p_y - dx[direction]
        if array[nx][ny] == 0:
            p_x = nx
            p_y = ny
        else:
            break
        turn_time = 0

print(count)