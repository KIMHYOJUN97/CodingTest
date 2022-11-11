T = int(input())

for t in range(1,T+1):
    fight = list(input())
    cnt = 0
    for f in fight:
        if f =='x':
            cnt+=1

    if(cnt >=8):
        print("#{} {}".format(t,"NO"))
    else:
        print("#{} {}".format(t,"YES"))