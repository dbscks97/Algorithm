from sys import stdin as s
import sys

sys.setrecursionlimit(10**6)

#s = open('input.txt','rt')



def dfs(data,li):
    global cnt

    if sum(li) == data :
        cnt+=1
        return 
    
    if sum(li) > data:
        return
    
    for i in range(1,4):
        li.append(i)
        dfs(data,li)
        li.pop()
                                             



n = int(s.readline())

list=[]

for i in range(n):
    
    a = int(s.readline())
    list.append(a)
    
    for i in list:
        cnt= 0
        dfs(i,[])

    print(cnt)