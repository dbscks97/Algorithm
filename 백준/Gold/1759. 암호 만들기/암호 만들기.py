from sys import stdin as s

L,C = map(int,s.readline().split())
arr=list(map(str,s.readline().split()))
alpha=['a','e','i','o','u']
arr.sort()
answer=[]
result=[]
count=0
another_count=0
def dfs(v, answer):
  if len(answer) == L:
    count=0
    another_count=0
    for i in answer:
        if i in alpha:
            count+=1
        else:
            another_count+=1
    
    if count>=1 and another_count>=2:
        result.append(answer.copy())
              
    return
  if v == C:
    return
  answer.append(arr[v])
  dfs(v+1, answer)
  answer.pop()
  dfs(v+1, answer)
 
dfs(0, [])

for i in range(len(result)):
    print(''.join(result[i]))