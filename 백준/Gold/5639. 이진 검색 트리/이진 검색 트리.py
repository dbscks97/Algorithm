from sys import stdin as s
import sys
sys.setrecursionlimit(10 ** 9)

#s = open('input.txt','rt')


def postorder(start,end):
    
    if start > end:
        return
    
    mid = end+1
    
    for i in range(start+1,end+1):
        if arr[i] > arr[start]:
            mid = i
            break
    
    postorder(start+1,mid-1)
    postorder(mid,end)
    print(arr[start])
     

if __name__=='__main__':
    
    arr=[]
    while True:
        try:
            arr.append(int(s.readline().strip()))
        except:
            break
    
    postorder(0,len(arr)-1)