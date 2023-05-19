from sys import stdin as s

N = int(s.readline())
arr = list(map(int,s.readline().split()))
num = int(s.readline())

start=0
end=max(arr)

while start<=end:
    mid = (start + end) //2
    result=0
    for i in arr:
        if mid < i:
            result+=mid
        else:
            result+=i
    
    if result>num:
        end = mid-1
    else:
        start = mid+1

    
print(end)