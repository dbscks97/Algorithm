import heapq as hq
def solution(n, k, enemy):
    answer = 0
    heap = []
    
    for i in range(len(enemy)):
        hq.heappush(heap,enemy[i])
        if k>=len(enemy):
            return len(enemy)
        
        if len(heap)>k:
            n-=hq.heappop(heap)
            answer+=1
        if n <0:
            answer-=1
            break
    answer+=k
    return answer