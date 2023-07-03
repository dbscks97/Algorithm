from sys import stdin as s

n=s.readline()

result = 1000000
for i in range(int(n)):
    length = len(str(i))
    cnt = 0
    for j in range(length):
        a = str(i)
        cnt += int(a[j])
    
    if cnt + i == int(n):
        result = min(result, i)

if result == 1000000:
    print(0)
else:
    print(result) 