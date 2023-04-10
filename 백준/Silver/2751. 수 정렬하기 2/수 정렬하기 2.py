import sys

num = int(sys.stdin.readline())
n = []

for i in range(num):
     a = int(sys.stdin.readline())
     n.append(a)

n.sort()

for i in n:
    print(i)
    
