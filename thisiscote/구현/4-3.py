#왕실의 나이트

str1 = input()
a = int(ord(str1[0])) - int(ord('a'))
b = int(str1[1])-1
count = 0
dx = [2,1,-2,-1,2,1,-2,-1]
dy = [1,2,1,2,-1,-2,-1,-2]

for i in range(8):
    nx = a+dx[i]
    ny = b+dy[i]
    if nx >=0 and nx <8 and ny >=0 and ny <8:
        count += 1

print(count)
