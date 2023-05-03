from sys import stdin as s

n = int(s.readline())

arr = list(map(int,s.readline().split()))
arr.sort(reverse=True)
total=0

for i in range(len(arr)):
    if len(arr)==1:
        break
    arr[0]=arr[0] + (arr[-1]/2)
    total +=arr[0]
    arr.pop()
    
    
print(arr[0])