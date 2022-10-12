import sys
input = sys.stdin.readline

words = list(input().rstrip())
reversed_word = []
answer = []
flag = 0
for word in words:
    if word == '<':
        while(reversed_word):
            answer.append(reversed_word.pop())
        flag = 1
        answer.append(word)
        continue
    if word =='>':
        answer.append(word)
        flag = 0
        continue
    if flag ==1:
        answer.append(word)
        continue
    
    if word != ' ':
        reversed_word.append(word)
    else:
        while(reversed_word):
            answer.append(reversed_word.pop())
        answer.append(' ')
if(reversed_word):
    while(reversed_word):
            answer.append(reversed_word.pop())
print("".join(answer))