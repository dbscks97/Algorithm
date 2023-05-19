from sys import stdin as s

N,K =map(int,s.readline().split())
arr=list(map(int,s.readline().split()))
ans=[]

for i in range(1,N):
    ans.append(arr[i]-arr[i-1])

ans.sort(reverse=True)

first = arr[-1] - arr[0] 

for i in range(K-1):
    first -= ans[i]

print(first)

