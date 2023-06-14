import heapq
def solution(scoville, K):
    answer = 0
    heap=[]
    for i in scoville:
        heapq.heappush(heap,i)
    
    for i in range(len(heap)):
        if heap:
            a=heapq.heappop(heap)
        if a>=K:
            break
        if heap:
            b=heapq.heappop(heap)
        c = a + (b*2)
        heapq.heappush(heap,c)
        answer+=1
        
    if answer == len(scoville):
        answer = -1

    return answer