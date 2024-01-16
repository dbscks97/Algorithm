from sys import stdin as s

T = int(s.readline())

for i in range(T):
    N = int(s.readline().strip())
    tree = list(map(int,s.readline().split()))
    
    tree.sort()
    res = 0
    for i in range(2, N):
        res = max(res, abs(tree[i] - tree[i-2]))
    print(res)
    