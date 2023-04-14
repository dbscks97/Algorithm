import sys
from sys import stdin as s

#s = open('input.txt','rt')


def multi(A,B,C):
    
    if B == 1: 
        return A%C
    
    temp = multi(A, B//2,C)
    
    if B % 2== 0:
        return temp * temp % C
    else:
        return temp * temp * A % C
    



if __name__=='__main__':
    A,B,C=map(int,s.readline().split())
    
    print(multi(A,B,C))
        