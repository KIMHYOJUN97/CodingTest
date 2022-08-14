#쇠막대기가 생기는 건 무조건 n+1개
st = list(input())
print(st)
laser = []
#index -1
pipeline = []
pipeline_stack = []
answer = 0
for i,s in enumerate(st):
    if s == '(':
        if st[i+1] == ')':
            laser.append(i)
        else:
            pipeline.append(i)
    else:
        if st[i-1]=='(':
            continue
        else:
            pipeline_stack.append([pipeline.pop(),i])

for pipe in pipeline_stack:
    cnt =0
    for l in laser:
        if pipe[0] <l<pipe[1]:
            cnt += 1
    answer += (cnt+1)

print(cnt)