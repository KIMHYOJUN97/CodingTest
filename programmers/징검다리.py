#binary search
#LV4

#완전 탐색?
#순열 사용하여 하나씩 땡기기

def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    left = 0
    right = distance+1
    rocks.append(distance)
    while left < right:
        mid = (left+right)//2
        remove_cnt = 0
        cur = 0
        for rock in rocks:
            if rock - cur < mid:
                remove_cnt += 1
            else:
                cur = rock
        if remove_cnt < n+1:
            left = mid+1
        else:
            right = mid
    
    answer = left - 1
    return answer