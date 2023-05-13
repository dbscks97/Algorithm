from sys import stdin as s
N = int(s.readline())
arr =list(map(int,s.readline().split()))
ans = []
arr.sort()

if len(arr) %2==0:
    print(arr[(len(arr)//2)-1])
else:
    print(arr[len(arr)//2])

