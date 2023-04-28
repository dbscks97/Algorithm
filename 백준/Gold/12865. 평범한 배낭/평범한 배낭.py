from sys import stdin as s

N,K = map(int,s.readline().split())

arr=[[0]*(K+1) for _ in range(N+1)]

graph = [[0,0]]+[list(map(int,s.readline().split())) for _ in range(N)]


for i in range(1,N+1):
    for j in range(1,K+1):
        weight = graph[i][0]
        value = graph[i][1]
             
        if j < weight:
            arr[i][j] = arr[i-1][j]
        else:
            arr[i][j] = max(value + arr[i-1][j-weight],arr[i-1][j])

print(arr[N][K])
