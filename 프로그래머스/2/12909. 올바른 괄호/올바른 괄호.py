from collections import deque
def solution(s):
    ss = list(s)
    stack = deque()
    while ss:
        gualho = ss.pop()
        if len(stack) >= 1 and stack[0] + gualho == ')(':
            stack.popleft()
        else:
            stack.append(gualho)
    if len(stack) >= 1:
        return False
    else:
        return True