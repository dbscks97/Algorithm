from sys import stdin as s
result = [] 

N = int(s.readline())

for i in range(N):
    arr = s.readline().strip()
    
    arr_len = len(arr)
    count = 0
    for j in range(arr_len):
        if arr[j] == '0' or arr[j] == '1' or arr[j] == '2' or arr[j] == '3' or arr[j] == '4' or arr[j] == '5' or arr[j] == '6' or arr[j] == '7' or arr[j] == '8' or arr[j] == '9':
            count += int(arr[j])
    
    result.append((arr_len,count,arr))

result.sort(key=lambda x:(x[0],x[1],x[2]))

for i in range(len(result)):
    print(result[i][2])