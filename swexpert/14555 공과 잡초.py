T = int(input())

for t in range(1,T+1):
    cnt = 0
    board = list(input())
    for i in range(len(board)-1):
        if(board[i]=='('):
            if board[i+1]=='|':
                cnt+=1
            else:
                continue
        elif(board[i]==')'):
            cnt+=1
    if(board[-1]==')'):
        cnt+=1
    
    print("#{} {}".format(t,cnt))