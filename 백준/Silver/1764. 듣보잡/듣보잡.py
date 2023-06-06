from sys import stdin as s

arr=[]
arr2=[]
N,M = map(int,s.readline().split())

for i in range(N):
    a=str(s.readline().rstrip())
    arr.append(a)

for i in range(M):
    b=str(s.readline().rstrip())
    arr2.append(b)

answer = list(set(arr)&set(arr2))
answer.sort()
print(len(answer))
for i in answer:
    print(i)