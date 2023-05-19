from sys import stdin as s
n, m = map(int, s.readline().split())


arr = []
for _ in range(n):
    arr.append(int(s.readline()))

arr.sort()
left, right = 0, 0
result = int(2e9)

while left <= right and right < n: 
    if arr[right]-arr[left] < m:   
        right += 1
 
    else:   
        result = min(result, arr[right]-arr[left])    
        left += 1

print(result)