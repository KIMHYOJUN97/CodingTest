from email.policy import default


n =int(input())
hours = 23 # 3 13 23 00~23
minutes = 59 # 3 13 23 33 43 53  00~59 -6 => 54
seconds = 59 # 3 13 23 33 43 53  00~59

default = (60 * 6 + 60 * 6 - 36 )
all_time = 3600
count = (54 * 6 + 6*60)*21 + 3600 * 3
if(n <3):
    print(default*n)
elif(n >=3 and n <13):
    print(default*(n-1)+all_time)
elif(n >=13 and n<23):
    print(default*(n-2) + all_time*2)
else:
    print(count)

#책 풀이

n = int(input())
count = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count += 1

print(count)