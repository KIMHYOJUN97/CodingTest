T = int(input())

for t in range(1,T+1):
    n = int(input())
    lst = list(str(n))
    num_list = [n]
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            lst[i],lst[j] = lst[j],lst[i]
            tmp = ''
            for k in range(len(lst)):
                tmp += lst[k]
            lst[i],lst[j] = lst[j],lst[i]
            if(tmp==str(int(tmp))):
                num_list.append(int(tmp))
    print("#{} {} {}".format(t,min(num_list),max(num_list)))