#딕셔너리 내에서 정렬
#람다식 배우기

#많이 재생된 장르 고르기
#장르 내에서 많이 재생된 노래 고르기
#인덱스 번호는 앞에서부터
def solution(genres, plays):
    answer = []
    genres_count = {}
    dict = {}
    for gen in genres:
        if genres_count[gen]:
            genres_count[gen] += 1
        else:
            genres_count[gen] = 0

    
    for i in range(len(genres)):
        dict[genres[i]].append(plays[i])
    
    max = 0
    max_genres = ""
    while dict:
        lst = []
        lst_max = 0
        index_max =0
        for music in dict:
            music.value().sort()
            if sum(music.value()) >max:
                max = sum(music.value())
                max_genres = music
        for i in range(len(genres)):
            if genres[i] == max_genres:
                lst.append([i,plays[i]])
            
        lst.sort(key=lambda x: (x[1], x[0]))
        if(len(lst) >=2):
            for i in range(2):
                answer.append(lst[i][0])
        else:
            answer.append(lst[0][0])
        
        del dict[max_genres]

        

    return answer


def solution(genres, plays):
    answer = []
    temp = []
    total_genre_d = {}

    temp = [[genres[i], plays[i], i] for i in range(len(genres))]   # [장르, 재생횟수, 고유 번호] 리스트
    temp = sorted(temp, key=lambda x: (x[0], -x[1], x[2]))  # 많이 재생될수록, 같다면 고유번호가 낮을수록

    for g in temp:  # {장르 : 총 재생횟수} 딕셔너리 생성
        if g[0] not in total_genre_d:
            total_genre_d[g[0]] = g[1]
        else:
            total_genre_d[g[0]] += g[1]
    
    total_genre_d = sorted(total_genre_d.items(), key = lambda x: -x[1])    # 재생횟수가 많은 순서로 장르 정렬
    
    for i in total_genre_d: # 같은 장르 내에서는 최대 2곡까지 조건대로 수록
        count = 0
        for j in temp:
            if i[0] == j[0]:
                count += 1
                if count > 2:
                    break
                else:
                    answer.append(j[2])

    return answer