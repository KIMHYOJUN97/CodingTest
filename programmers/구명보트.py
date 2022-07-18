#Greedy
#LV2
#boat에 2명밖에 못탐 문제 잘 읽기

# 20 30 50 50 50 50 70 80 maybe 5?
# 0  1  2  3  4  5  6  7
def solution(people, limit):
    answer = 0
    people.sort()
    i ,j = 0,len(people)-1
    while i<=j:
        answer+=1
        if people[j]+people[i] <=limit:
            i +=1
        j -=1
    return answer
    