#Programmers Greedy
#LV3

def solution(routes):
    answer = len(routes)
    min_route = 30000
    max_route = -30001
    for r in routes:
        if min(r[0],r[1])<min_route:
            min_route=min(r[0],r[1])
        if max(r[0],r[1]) >max_route:
            max_route=max(r[0],r[1])
    checked = [[0] for i in range(len(routes))]
    camera = [i for i in range(min_route,max_route)]
    

    return answer

#[-20 -15] [-18 -13] [-14 -5] [-5 -3]
def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[1])
    leng = len(routes)
    checked = [0] * leng

    for i in range(leng):
        if checked[i] == 0:
            camera = routes[i][1] # 진출 지점에 카메라를 갱신
            answer += 1
        for j in range(i+1, leng):
            if routes[j][0] <= camera <= routes[j][1] and checked[j] == 0:
                checked[j] = 1
    return answer

#[-20 -15] [-18 -13] [-14 -5] [-5 -3]
def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1]) # routes를 차량이 나간 지점 (진출) 기준으로 정렬
    camera = -30001 # -30001부터 카메라 위치를 찾습니다.

    for route in routes:
        if camera < route[0]:
            answer += 1
            camera = route[1]
    return answer

def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1]) # routes를 차량이 나간 지점 (진출) 기준으로 정렬
    camera = -30001 # -30001부터 카메라 위치를 찾습니다.

    for route in routes:
        if camera < route[0]:
            answer += 1
            camera = route[1]
    return answer
    
routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
#-20 -18 -15 -14 -13 -5 -3