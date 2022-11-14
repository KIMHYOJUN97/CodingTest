# T = int(input())

# for t in range(1,T+1):
#     n,p,g = map(int,input().split())
#     flag_d = 0
#     if p!=0:
#         for i in range(1,n+1):
#             if(i * p/100 % 1 == 0):
#                 flag_d = 1
#                 break
#     else:
#         if g!=0:
#             print("#{} {}".format(t,"Broken"))
#         else:
#             print("#{} {}".format(t,"Possible"))
#         continue
#     if(flag_d==1):
#         if(g == 100):
#             if(p==100):
#                 print("#{} {}".format(t,"Possible"))
#             else:
#                 print("#{} {}".format(t,"Broken"))
#         else:
#             print("#{} {}".format(t,"Possible"))
#     else:
#         print("#{} {}".format(t,"Broken"))

T = int(input())

for t in range(1,T+1):
    n,p,g = map(int,input().split())
    if p != 0 and g ==0:
        print("#{} {}".format(t,"Broken")) 
        continue
    elif p != 100 and g ==100:
        print("#{} {}".format(t,"Broken"))
        continue
    else:
        flag = 0
        for i in range(1,n+1):
            if(i * p/100%1 ==0):
                print("#{} {}".format(t,"Possible"))
                flag = 1
                break
    if(flag==0):
        print("#{} {}".format(t,"Broken"))