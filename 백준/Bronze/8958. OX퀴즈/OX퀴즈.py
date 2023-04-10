import sys


n = int(sys.stdin.readline())


for i in range(n):
    a = list(sys.stdin.readline())
    cnt = 0
    sum = 0
    
    for j in a:
        if j == 'O':
            cnt += 1
            sum += cnt
        else:
            cnt = 0
    print(sum)