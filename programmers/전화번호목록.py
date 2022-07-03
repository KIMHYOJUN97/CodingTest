#시간 초과

def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)):
        k1 = len(phone_book[i])
        for j in range(i+1,len(phone_book)):
            if phone_book[i] in phone_book[j][:k1]:
                return False
    return answer  

#해쉬 사용해서 풀이
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer