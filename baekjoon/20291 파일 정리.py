import sys
from collections import defaultdict
input = sys.stdin.readline
n = int(input())
answer = defaultdict(int)
words = []
for i in range(n):
    question = list(input().rstrip())
    index = 0
    for j in range(len(question)):
        if question[j]=='.':
            index = j
    answer["".join(question[index+1:])]+=1
    words.append("".join(question[index+1:]))
s1 = set(words)
words = list(s1)
words.sort()
for word in words:
    print(word,answer[word])