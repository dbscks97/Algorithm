from sys import stdin as s
from collections import deque

q=deque()
ans=[0]*10
n = list(map(int,s.readline().strip()))

for i in range(len(n)):
    q.append(n[i])
    


while q:
    i = q.popleft()
    for j in range(10):
        if (i==6 or i==9) and i==j:
            ans[9]+=1
        elif i == j:
            ans[j]+=1
            

if ans[9]%2==0:
    ans[9]=ans[9]//2
else:
    ans[9]=(ans[9]//2)+1

print(max(ans))