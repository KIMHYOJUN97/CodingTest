#거대 괄호를 나눠야한다
#숫자를 따로 포함하는 stack을 하나 더 만들어준다.
#끝')]' 과 시작'(['이 오면 더하기 <=이게 가장 문제
import sys

def solution(question):
    stack = []
    num_stack = []
    flag = 0
    for i,q in enumerate(question):
        if q == '[':
            stack.append('[')
        elif q == '(':
            stack.append('(')
        elif q == ']':
            if i < len(question)-2 and question[i+1]:
                if question[i+1] == '(' or question[i+1] == '[':
                    flag = 1
            if stack.pop()!='[':
                return 0
            else:
                if stack or len(num_stack)==0:
                    num_stack.append(3)
                else:
                    num_stack.append(num_stack.pop()*3)
                if flag == 1 and len(num_stack)>1 and i < len(question)-2 and question[i+1] != ')' and question[i+1] != ']':
                    num_stack.append(num_stack.pop()+num_stack.pop())
                    flag = 0
                
        else:
            if i < len(question)-2 and question[i+1]:
                if question[i+1] == '(' or question[i+1] == '[':
                    flag = 1
            if stack.pop() !='(':
                return 0
            else:
                if stack or len(num_stack)==0:
                    num_stack.append(2)
                else:
                    num_stack.append(num_stack.pop()*2)
                if flag == 1 and len(num_stack)>1 and i < len(question)-2 and question[i+1] != ')' and question[i+1] != ']':
                    num_stack.append(num_stack.pop()+num_stack.pop())
                    flag =0
    
    return num_stack[0]
            
    

s = sys.stdin.readline()
question = s.rstrip()
print(solution(question))