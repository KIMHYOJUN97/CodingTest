#LV1

def solution(sizes):
    answer = 0
    width_max = 0
    vertical_max = 0
    answer_list = []

    for size in sizes:
        if size[0] >width_max:
            width_max=size[0]
        if size[1] >vertical_max:
            vertical_max=size[1]
    
    if width_max > vertical_max:
        for size in sizes:
            if size[0]<size[1] and size[0] < width_max:
                size[0],size[1] = size[1],size[0]
            answer_list.append(size[1])
        answer = max(answer_list)*width_max
    else:
        for size in sizes:
            if size[0]>size[1] and size[1] < vertical_max:
                size[0],size[1] = size[1],size[0]
            answer_list.append(size[0])
        answer = max(answer_list)*vertical_max

    return answer