from sys import stdin as s


N = int(s.readline())

arr=list(map(int,s.readline().split()))
dp=[1]*N
ans=[]
for i in range(N):  # 배열 길이만큼돈다.
    for j in range(i):  # 해당 배열 원소의 직전 원소까지 돈다.
        if arr[i] > arr[j]:  # 만약 해당 원소가 전 원소보다 크다면
            dp[i] = max(dp[i], dp[j] + 1)
            # 전 원소에 저장되어 있는 최장수열길이에서 +1 값과 저장되어있는 수열길이값을 비교해서 큰값을 대입
temp=max(dp)

for i in range(N-1,-1,-1):
    if dp[i] ==temp:
        ans.append(arr[i])
        temp-=1
ans.sort()
print(max(dp))
print(*ans)