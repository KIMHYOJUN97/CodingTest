T = 10

for t in range(1,T+1):
    n = int(input())
    graph = []
    for _ in range(100):
        graph.append(list(map(int,input().split())))
    row = []
    col = []
    cross = 0
    re_cross = 0
    for i in range(100):
        row_sum = 0
        col_sum = 0
        for j in range(100):
            row_sum += graph[i][j]
            col_sum += graph[j][i]

            if i==j:
                cross+=graph[i][j]
            if i+j == 99:
                re_cross+=graph[i][j]
        row.append(row_sum)
        col.append(col_sum)
    
    print("#{} {}".format(t,max(max(row),max(col),cross,re_cross)))