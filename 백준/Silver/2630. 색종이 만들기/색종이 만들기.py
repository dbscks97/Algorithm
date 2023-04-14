import sys
from sys import stdin as s

#s = open('input.txt','rt')


def paper(N,x,y):
    global white
    global blue
    
    color = board[x][y]
    
    for i in range(x,x+N):
        for j in range(y,y+N):
            if color != board[i][j]:
                paper(N//2,x,y)
                paper(N//2,x,y+N//2)
                paper(N//2,x+N//2,y)
                paper(N//2,x+N//2,y+N//2)
                return
            
    if color == 0:
        white +=1
    else:
        blue +=1

if __name__=='__main__':
    N=int(s.readline())

    board = [list(map(int,s.readline().split())) for _ in range(N)]
    white = 0
    blue = 0

    paper(N,0,0)
    print(white)
    print(blue)

    





