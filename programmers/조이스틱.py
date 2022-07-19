#Greedy
#LV2

#two pointer 형태로 풀기 가능?
from xmlrpc.client import MAXINT

def solution(name):
    # alpha = {'A':1,'B':2,'C':3,'D':4,'E':5,
    # 'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,
    # 'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,
    # 'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,
    # 'Y':25,'Z':26}
    # 13칸 기준
    #
    alpha = {}
    for i in range(26):
        alpha[chr(ord('A')+i)]=i+1
    left = 1
    target = name[0]
    answer = alpha[target]
    right = len(name)-1
    while left <=right:
        check_left=min(abs(alpha[target]-alpha[name[left]]),(alpha[left]+26-alpha[target])) #조이스틱을 앞으로만 땡길 때 걸리는 횟수
        check_right =min(abs(alpha[target]-alpha[name[right]]),(alpha[right]+26-alpha[target]))
        min_check_left = MAXINT
        min_check_right = MAXINT
        if(check_left <=check_right):
            answer += check_left
            left += 1
        else:
            answer += check_right+1
            right -=1
        
    return answer

def solution(name):
    # alpha = {'A':1,'B':2,'C':3,'D':4,'E':5,
    # 'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,
    # 'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,
    # 'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,
    # 'Y':25,'Z':26}
    # 13칸 기준
    answer = 0
    alpha = {}
    for i in range(26):
        alpha[chr(ord('A')+i)]=i
    
    direction = 0
    left = 0
    right = len(name)-1
    cnt = 0

    while left<=right:
        if direction ==0:
            answer += alpha[name[left]]
            cnt += 1
            left += 1
        else:
            answer += alpha[name[right]]
            right -=1
            cnt += 1
        if name[left] and name[left] == 'A' and name[right] != 'A':
            answer += alpha[name[right]]
            right -= 1
            cnt += 1
            direction = 1

    return answer

#다시 보기
def solution(name):
    answer = 0

    min_move = len(name)-1

    for i,char in enumerate(name):
        answer += min(ord(char)-ord('A'),ord('Z')-ord(char)+1)
        next = i + 1
        while next<len(name) and name[next]=='A':
            next += 1
        
        min_move=min([min_move,2*i+len(name)-next,i+2*(len(name)-next)])

    answer += min_move
    return answer