from sys import stdin as s

n=int(s.readline())
p = list(map(int,s.readline().split()))

p.sort()
answer=[0]*n
answer[0]=p[0]
for i in range(1,n):
    answer[i] = answer[i-1]+p[i]

print(sum(answer))