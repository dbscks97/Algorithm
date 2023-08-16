from sys import stdin as s
from collections import deque

k = int(s.readline())
sign = deque()
ans = []

a = s.readline().split()

for i in range(k):
    c = a[i]
    sign.append(c)



for _ in range(k):
    b = sign.popleft()
    temp_ans = []  

    if b == '<':
        if ans:
            for lst in ans:
                last_digit = lst[-1]
                for z in range(last_digit + 1, 10):
                    if z not in lst:
                    
                        temp_ans.append(lst + [z])
        else:
            for j in range(10):
                for z in range(j+1, 10):
                    temp_ans.append([j, z])

    elif b == '>':
        if ans:
            for lst in ans:
                last_digit = lst[-1]
                for z in range(last_digit):
                    if z not in lst:
                    
                        temp_ans.append(lst + [z])
        else:
            for j in range(10):
                for z in range(j):
                    temp_ans.append([j, z])

    ans = temp_ans  

ma = max(ans)
mi = min(ans)

ma_str = ''.join(map(str, ma))
mi_str = ''.join(map(str, mi))

print(ma_str)
print(mi_str)
                    
                
