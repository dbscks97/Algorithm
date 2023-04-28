from sys import stdin as s

N ,K = map(int,s.readline().split())
coins=[]
count = 0

for i in range(N):
    A=int(s.readline())
    coins.append(A)
    
coins.sort(reverse=True)


for coin in coins:
    count += K//coin
    K %=coin

print(count)