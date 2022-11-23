T = 10

def is_palin(tmp):
    if(tmp==tmp[::-1]):
        return True
    
    return False

for t in range(1,T+1):
    n = int(input())
    graph = []
    for _ in range(8):
        graph.append(list(input()))
    
    answer = 0
    for i in range(8):
        tmp = ''
        tmp2 = ''
        for j in range(8):
            if(len(tmp)<n):
                tmp += graph[i][j]
                tmp2 += graph[j][i]
            if(len(tmp)==n):
                if(is_palin(tmp)):
                    answer+=1
                if(is_palin(tmp2)):
                    answer+=1
            
                tmp=tmp[1:]
                tmp2=tmp2[1:]
    print("#{} {}".format(t,answer))