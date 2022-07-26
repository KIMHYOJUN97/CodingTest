#정렬
#LV2

#순열 시간초과
# from itertools import permutations

# def solution(numbers):
#     answer = ''
#     numbers = list(map(str,numbers))
#     per_list = list(permutations(numbers))
#     answer_list = []
#     for per in per_list:
#         tmp = ''
#         for p in per:
#             tmp += p
#         answer_list.append(tmp)
    
#     answer_list=list(map(int,answer_list))
#     answer = str(max(answer_list))

#     return answer

#3, 304  3304 3043  320 32 32320 32032  37 371  37371 37137
#어짜피 자리수는 0-9이니까 9개의 index 생성 후 큰 자리수대로 정렬?
#x[0] x[-1]>=x[0] int(x)
#값이 같으면 짧은쪽이 먼저=>전처리 해줘야함
def solution(numbers):
    answer = ''
    numbers = list(map(str,numbers))
    numbers.sort(key=lambda x:-int(x[0]))
    # answer_list = [['1' for i in range(5)]] * len(numbers)
    answer_list = [['1' for i in range(5)] for _ in range(len(numbers))] 
    i  = 0
    for num in numbers:
        j = 0
        for n in num:
            answer_list[i][j] = n
            j+=1
        answer_list[i][4] = len(num)
        i += 1
    #answer_list.sort(key=lambda x:(map(int,(x[0]),x[1],x[2],x[3])))
    answer_list.sort(key=lambda x:(-int(x[0]),int(x[1]),int(x[2]),int(x[3])))

    for ans in answer_list:
        for i in range(ans[4]):
            answer += ans[i]
    # while numbers:
    #     max = 0
    #     max_all = ''
    #     index = 0
    #     for i,num in enumerate(numbers):
    #         if int(num[0]) > max:
    #             max = int(num[0])
    #             max_all = num
    #             index = i
    #     answer_list.append([max_all,len(max_all)])
    #     numbers.pop(index)
    #len값 조사 중 x[0]값이 x[1]값보다 작은경우
    # answer_list.sort(key=lambda x:(x[1],-int(x[0])))

    # for ans in answer_list:
    #     answer += ans[0]
    answer = int(answer)
    return str(answer)

# print(solution([101, 10, 232, 23]))

def solution2(numbers):
    answer = ''
    numbers=list(map(str,numbers))
    print(numbers)
    numbers.sort(key=lambda x:x*3,reverse=True)
    print(numbers)
    for num in numbers:
        answer += num
    return str(int(answer))
# 2323210110

print(solution2([101, 10, 232, 23]))