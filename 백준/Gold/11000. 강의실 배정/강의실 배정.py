from sys import stdin as s
import heapq as hq

N=int(s.readline())
lecture =[]
answer=[]
cnt=1
for i in range(N):
    start, end = map(int,s.readline().split())
    lecture.append((start,end))

lecture.sort()
hq.heappush(answer,lecture[0][1])

for i in range(1,N):
    if lecture[i][0] < answer[0]:
        hq.heappush(answer, lecture[i][1])
    else:
        hq.heappop(answer)
        hq.heappush(answer,lecture[i][1])    
    
print(len(answer))