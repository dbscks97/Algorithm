from sys import stdin as s
from collections import deque

def check_left(T,dir):
    if T<1 or tire[T][2] == tire[T+1][6]:
        return
    
    if tire[T][2] != tire[T+1][6]:
        check_left(T-1,-dir)
        tire[T].rotate(dir)


def check_right(T,dir):
    if T>4 or tire[T][6] == tire[T-1][2]:
        return
    
    if tire[T][6] != tire[T-1][2]:
        check_right(T+1,-dir)
        tire[T].rotate(dir)

if __name__=="__main__":
    tire = deque()
    result = 0
    for i in range(4):
        a = deque(list(map(int,s.readline().strip())))
        tire.append(a)
    tire.appendleft([0])
    K = int(s.readline())
    
    for i in range(K):
        T,dir = map(int,s.readline().split())
        
        check_left(T-1,-dir)
        check_right(T+1,-dir)
        tire[T].rotate(dir)
    
for i in range(1,5):
    result += (2**(i-1)) * tire[i][0]

print(result)
