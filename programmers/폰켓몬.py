def solution(nums):
    answer = 0
    pick = len(nums)//2
    s1 = set(nums)
    lst = list(s1)

    if len(lst) >= pick:
        answer=pick
    else:
        answer = len(lst)
    return answer