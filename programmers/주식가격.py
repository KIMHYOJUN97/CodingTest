def solution(prices):
    answer = []
    for i in range(1, len(prices)):
        cur = prices[i - 1]
        cnt = 0
        for j in range(i,len(prices)):
            cnt += 1
            if cur > prices[j]:
                break
        answer.append(cnt)
    answer.append(0)
    return answer