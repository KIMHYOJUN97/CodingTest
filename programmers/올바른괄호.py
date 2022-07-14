#stack/queue

def solution(s):
    answer = True
    lst = list(s)
    stack = []
    for i in range(len(lst)):
        if not stack and lst[i] ==")":
            return False
        if lst[i] =="(":
            stack.append("(")
        else:
            if stack.pop()==")":
                return False
    if stack:
        return False
    return answer
        