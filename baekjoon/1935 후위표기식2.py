n = int(input())
question = list(input())
dictionary = dict()
st = []
num = []
for i in range(n):
    num.append(int(input()))
for i in range(26):
    dictionary[chr(ord('A')+i)]=i
while question:
    if question[0] !='*' and question[0] !='-' and question[0] !='+' and question[0] != '/':
        st.append(num[dictionary[question.pop(0)]])
    else:
        calculate = question.pop(0)
        last = st.pop()
        first = st.pop()
        answer = 0
        if calculate =='*':
            answer = (first*last)
        elif calculate =='+':
            answer = (first+last)
        elif calculate =='-':
            answer = (first-last)
        else:
            answer = (first/last)
        st.append(answer)
print("{:.2f}".format(st[0]))