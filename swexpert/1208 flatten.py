for t in range(1,11):
    chance = int(input())
    block = list(map(int,input().split()))
    while(chance >0):
        max_block = max(block)
        min_block = min(block)
        block[block.index(max_block)]-=1
        block[block.index(min_block)]+=1
        chance -= 1
    print("#{} {}".format(t,max(block)-min(block)))