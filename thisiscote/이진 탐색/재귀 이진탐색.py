#재귀 함수로 구현한 이진 탐색 소스코드
def binary_search(array,target,start,end):
    if start>end:
        return None
    mid = (start + end) //2
    #찾은 경우 인덱스 중앙
    if array[mid] == target:
        return mid
    #중간점의 값보다 찾고자 하는 값이 적은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array,target,start,mid-1)
    #중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array,target,mid+1,end)

