#퀵 정렬
#O(NlogN) 보장

array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array,start,end):
    if start >= end:
        return
    pivot = start
    left = start+1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right >start and array[right] >= array[pivot]:
            right -= 1
        #엇갈리면 작은 데이터와 피벗 교체
        if left > right:
            array[right],array[pivot] = array[pivot],array[right]
        #엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
        else:
            array[left],array[right] = array[right],array[left]
        
    #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)

#파이썬을 이용한 퀵 정렬

def quick_sort2(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort2(left_side)+[pivot]+quick_sort2(right_side)
