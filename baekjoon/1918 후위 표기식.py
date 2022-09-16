#우선순위
#() >> * / >> + -

# infix = list(input())
# postfix = []
# opstack = []
# for i in infix:
#     if i == "*" or i == "/" or i == "(":
#         opstack.append(i)
#     elif i == "+" or i == "-":
#         if len(opstack) == 0:
#             opstack.append(i)
#         else:
#             for j in range(len(opstack)):
#                 if opstack[-1]=="*" or opstack[-1] == "/":
#                     postfix.append(opstack.pop())
#                 opstack.append(i)
#     elif i == ")":
#         while(opstack[-1] !="("):
#             postfix.append(opstack.pop())
#         opstack.pop()
#     else:
#         postfix.append(i)
# while(len(opstack)!=0):
#     postfix.append(opstack.pop())

# for i in range(len(postfix)):
#     print(postfix[i],end='')

a=input()
stack=[]
res=''
op = ['(',')','+','-','*','/']
for x in a:
    if x not in op:
        res+=x
    else:
        if x=='(':
            stack.append(x)
        elif x=='*' or x=='/':
            while stack and (stack[-1]=='*' or stack[-1]=='/'):
                res+=stack.pop()
            stack.append(x)
        elif x=='+' or x=='-':
            while stack and stack[-1]!='(':
                res+=stack.pop()
            stack.append(x)
        elif x==')':
            while stack and stack[-1]!='(':
                res+=stack.pop()
            stack.pop()
while stack:
    res+=stack.pop()
print(res)