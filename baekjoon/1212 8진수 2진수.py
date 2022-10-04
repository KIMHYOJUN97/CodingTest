# import sys
# input = sys.stdin.readline

# n = list(map(int,input().rstrip()))
# ten=0
# for i in range(len(n)):
#     ten += n[len(n)-i-1]*8**(i)
# binary_list = []
# while(True):
#     if(ten==1):
#         binary_list.append(1)
#         break
#     if(ten%2==0):
#         binary_list.append(0)
#         ten = ten/2
#     else:
#         binary_list.append(1)
#         ten =ten//2
# for i in range(len(binary_list)):
#     print(binary_list[len(binary_list)-i-1],end='')

print(bin(int(input(), 8))[2:])