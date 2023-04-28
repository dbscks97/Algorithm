from sys import stdin as s

T = int(s.readline())



for i in range(T):
    
    N = int(s.readline())
    coin = list(map(int,s.readline().split()))
    M = int(s.readline())
    d = [0]*(M+1)
    d[0]=1
    
    for coins in coin:
        for j in range(M+1):
            if j>=coins:
                d[j]+=d[j-coins]

    print(d[M])
