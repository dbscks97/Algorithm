from sys import stdin as s

n=int(s.readline())
dp=[0]*(n+1)
arr=[0]+list(map(int,s.readline().split()))
dp[1]=arr[1]
for i in range(2,n+1):
    if dp[i-1]+arr[i]>0:
        dp[i]=dp[i-1]+arr[i]


if sum(dp) <0:
    if max(arr[1:])==0:
        print(0)
    else:
        print(max(arr[1:]))
else:
    print(max(dp))
