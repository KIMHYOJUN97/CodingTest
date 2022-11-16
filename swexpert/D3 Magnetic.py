#String 처리
#움직임을 일일히 계산 X

T = 10

def check_A(position):
    for i in range(position[0]+1,100):
        if(graph[i][position[1]]=='2'):
            return True
    
    return False

def check_B(position):
    for i in range(position[0]-1,-1,-1):
        if(graph[i][position[1]]=='1'):
            return True
    
    return False

for t in range(1,T+1):
    graph = []
    n = int(input())
    for _ in range(100):
        graph.append(list(input().split()))
    
    for i in range(100):
        for j in range(100):
            if(graph[i][j]=='1'):
                if(not check_B([i,j])):
                    graph[i][j] = '0'
            if(graph[i][j]=='2'):
                if(not check_A([i,j])):
                    graph[i][j] = '0'
    
    answer = []
    for i in range(100):
        tmp = ''
        for j in range(100):
            if(graph[j][i]!='0'):
                tmp += graph[j][i]
        answer.append(tmp)
    sum = 0
    for ans in answer:
        sum += ans.count('12')
    print("#{} {}".format(t,sum))