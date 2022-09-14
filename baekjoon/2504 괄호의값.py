question = list(input())
stack = []
string_stack = []
answer = 0

while question:
    string = question.pop(0)
    if string == '(':
        string_stack.append('(')
    elif string == ')':
        if string_stack[-1]=='(':
            string_stack.pop()
            stack.append(2)
        else:
            if string_stack[-1] =='[':
                answer = 0
                break
            else:
                
    # next_string = question.pop(0)
    # if string == '(':
    #     if next_string == ')':
    #         stack.append(2)
    #     elif next_string == '[':
    #         string_stack.append('[')
    #     elif next_string == '(':
    #         string_stack.append('(')
    #     else:
    #         answer = 0
    #         break
    # elif string =='[':
    #     if next_string ==']':
    #         stack.append()