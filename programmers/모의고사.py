#LV1
#완전 탐색

def solution(answers):
    answer = []
    num_list = [0,0,0]

    first_people = [1,2,3,4,5] #5
    second_people=[2,1,2,3,2,4,2,5] #8
    third_people=[3,3,1,1,2,2,4,4,5,5] #10

    for i in range(len(answers)):
        if answers[i]==first_people[i%len(first_people)]:
            num_list[0] += 1
        if answers[i]==second_people[i%len(second_people)]:
            num_list[1] += 1
        if answers[i]==third_people[i%len(third_people)]:
            num_list[2] += 1
    
    max_list = max(num_list)
    for i in range(3):
        if max_list==num_list[i]:
            answer.append(i+1)
    return answer

print(solution([1,2,3,4,5]))