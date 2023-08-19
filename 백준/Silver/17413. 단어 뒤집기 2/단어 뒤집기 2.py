from sys import stdin as s
from collections import deque

stack = []
tag = False
a = str(s.readline().rstrip())
ans=''

for i in a:
    if i == " ":
        while stack:
            ans += stack.pop()
        ans += i
    
    elif i == "<":
        while stack:
            ans += stack.pop()
        tag = True
        ans += i
    
    elif i == ">":
        tag = False
        ans += i
    
    elif tag:
        ans += i
    
    else:
        stack.append(i)

while stack:
    ans += stack.pop()
    
print(ans)

