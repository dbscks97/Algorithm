from sys import stdin as s
import heapq as hq

#s = open('input.txt','rt')
heap = []
h_o_list = []
N = int(s.readline())
h_o = [sorted(list(map(int,s.readline().split())))for _ in range(N)]
h_o.sort(key=lambda x: x[1]) #lambda 함수 사용해서 두번째 열 기준으로 오름차순 
d = int(s.readline())

for i,j in h_o:
    if abs(i-j) <=d:
        h_o_list.append((i,j))   
        
answer = 0


for i,j in h_o_list:
    
    
    while heap and heap[0][0] < j-d:
        hq.heappop(heap)
        
    if j-i <= d:
        hq.heappush(heap,(i,j))
        answer = max(answer,len(heap))
        


print(answer)      