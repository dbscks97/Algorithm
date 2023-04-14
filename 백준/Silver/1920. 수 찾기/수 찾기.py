from sys import stdin as s
import sys

#s = open('input.txt','rt')


def binary(start,end,arr,target):
    
    mid = (start+end)//2
    
    if start>end:
        empty_list.append(0)
        return -1

    if arr[mid]== target:
        empty_list.append(1)
        return mid
    
    elif arr[mid] < target:
        return binary(mid+1,end,arr,target)
    
    else:
        return binary(start,mid-1,arr,target)
        

if __name__=='__main__':
    
    
    N = int(s.readline())
    

    arr=list((map(int,s.readline().split())))
    arr.sort()
    M = int(s.readline())
       
    find_list=list((map(int,s.readline().split())))
        
    empty_list = []
    
    start = 0
    end = len(arr)-1
          
    
    for i in find_list:
         binary(0,end,arr,i)
        
    for i in empty_list:
        print(i)