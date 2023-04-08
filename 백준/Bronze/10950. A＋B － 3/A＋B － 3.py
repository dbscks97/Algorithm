import sys
read = sys.stdin.readline()

a = int(read)

for i in range(a):
    read = sys.stdin.readline()
    x,y = map(int,read.split())
    print(x+y)