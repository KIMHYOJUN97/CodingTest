def is_palin(palin):
    if(palin == palin[::-1]):
        return 1
    else:
        return 0

for t in range(1,11):
    graph =[]
    answer = set()
    n = int(input())
    for i in range(100):
        graph.append(list(input()))
    for i in range(100):
        tmp = ""
        tmp2 = ""
        for j in range(100):
            tmp += graph[i][j]
            tmp2 += graph[j][i]
            if(is_palin(tmp)):
                answer.add(tmp)
            if(is_palin(tmp2)):
                answer.add(tmp2)
    print(answer)
    print("#{} {}".format(t,len(answer)))
    