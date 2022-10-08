import sys
input = sys.stdin.readline

money = int(input())
price = list(map(int,input().split()))
jun_money = money
seong_money = money
jun_cnt = 0
seong_cnt = 0
up_cnt = 0
down_cnt = 0
result = []
for i in range(len(price)):
    if(jun_money/price[i]>0):
        jun_cnt += int(money/price[i])
        jun_money -= price[i]*(int(money/price[i]))
result.append(jun_money+jun_cnt*price[-1])
for i in range(1,len(price)):
    if(price[i-1]<price[i]):
        up_cnt+=1
        down_cnt = 0
    elif(price[i-1]>price[i]):
        up_cnt = 0
        down_cnt+=1
    else:
        up_cnt = 0
        down_cnt = 0
    if(up_cnt ==3):
        seong_money += seong_cnt*price[i]
        seong_cnt = 0
        up_cnt-=1
    if(down_cnt ==3):
        seong_cnt += int(seong_money/price[i])
        seong_money -= price[i]*int(seong_money/price[i])
        down_cnt-=1
result.append(seong_cnt*price[-1]+seong_money)
if(result[0]>result[1]):
    print("BNP")
elif(result[0]<result[1]):
    print("TIMING")
else:
    print("SAMESAME")


