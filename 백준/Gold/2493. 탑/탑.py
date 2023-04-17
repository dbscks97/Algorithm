from sys import stdin as s
from collections import deque
#s = open('input.txt','rt')


stack = deque()


N = int(s.readline())
n_list =list(map(int,s.readline().split()))
ans = [0] * N



for i in range(N):
    h = n_list[i]
    
    while stack and n_list[stack[-1]] <h:
        stack.pop()
        
    if stack:
        ans[i] = stack[-1]+1
    
    stack.append(i)

print(' '.join(list(map(str,ans)))) # 형식 맞춰서 입력하는법 

    
        
   
