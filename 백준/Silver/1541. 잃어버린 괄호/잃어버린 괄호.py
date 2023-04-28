from sys import stdin as s

a = s.readline().split('-')
answer=[]
for i in a:
    sum = 0
    b=i.split('+')
    
    for j in b:
        sum += int(j)
    answer.append(sum)

n = answer[0]
for i in range(1,len(answer)):
    n -= answer[i]

print(n)
