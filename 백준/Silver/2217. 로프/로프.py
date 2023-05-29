from sys import stdin as s

N=int(s.readline())
arr=[]
answer=0
for i in range(N):
    a=int(s.readline())
    arr.append(a)
arr.sort(reverse=True)

for i in range(1,len(arr)+1):
    w = i * arr[i-1]
    answer = max(answer,w)

print(answer)