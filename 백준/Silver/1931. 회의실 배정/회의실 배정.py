from sys import stdin as s

N = int(s.readline())
arr =[]
for i in range(N):
    A,B = map(int,s.readline().split())
    arr.append((A,B))

arr.sort(key=lambda x:(x[1],x[0]))
cnt =1 
ans = arr[0][1]
for i in range(1,N):    
    if ans<=arr[i][0]:
        cnt+=1
        ans=arr[i][1]
        
    
print(cnt)