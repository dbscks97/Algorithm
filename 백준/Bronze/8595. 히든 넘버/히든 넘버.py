from sys import stdin as s
n = int(s.readline())

arr = list(map(str,s.readline().strip()))
result = []
answer = 0

for i in range(len(arr)):
    if arr[i].isdigit():
        result.append(arr[i])
        if len(result) == 6:
            a = "".join(result)
            answer += int(a)
            result.clear()
    else:
        if result:
            a = "".join(result)
            answer += int(a)
        result.clear()

if result:  
    a = "".join(result)
    answer += int(a)
    
print(answer)
        
        