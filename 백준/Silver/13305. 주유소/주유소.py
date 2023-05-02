from sys import stdin as s

n = int(s.readline())
road = list(map(int,s.readline().split()))
oil = list(map(int,s.readline().split()))

answer = [0] * n
ans = oil[0]
answer[0] = road[0] * oil[0]

for i in range(1,n-1):
    if ans > oil[i]:
        ans = oil[i]
    
    answer[i] = road[i] * ans
    
print(sum(answer))