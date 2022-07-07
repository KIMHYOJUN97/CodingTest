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