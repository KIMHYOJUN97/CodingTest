#LV3
#binary search

def solution(n, serving_times):
    n_aver = n // len(serving_times) if n % len(serving_times) == 0 else n // len(serving_times) + 1
    start = min(min(serving_times) * n, min(serving_times) * n_aver)
    end = min(min(serving_times) * n, max(serving_times) * n_aver)
    
    res_list = list(range(start, end+1))
    mid_idx = len(res_list)
    
    n_each = n_aver
    while len(res_list) != 1:
        mid_idx = len(res_list)//2
        mid = res_list[mid_idx]
        if (mid > min(serving_times) * n_each):
            n_each = mid // min(serving_times) if mid % min(serving_times) == 0 else mid // min(serving_times) + 1
        else:
            n_each -= 1
            if (mid <= max(serving_times) * (n-n_each)):
                res_list = res_list[mid_idx:]
            else :
                res_list = res_list[:mid_idx]
        
    return res_list[0]