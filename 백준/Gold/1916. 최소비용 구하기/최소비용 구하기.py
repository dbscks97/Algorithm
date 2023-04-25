from sys import stdin as s
import heapq


def dijkstra(graph,start):
    # 우선순위 큐 생성
    heap = []
    # 출발점에서 부터 노드까지의 비용을 저장할 배열
    distances = [INF] * (N+1)
    #1에서 1까지의 거리는 0이므로 0저장
    distances[start]=0
    #우선순위 큐에 현재 start에 해당하는 dist와 노드 저장 
    heapq.heappush(heap,[distances[start],start])
    
    
    while heap:
        #heap 에 들어있는 값을 빼서 node,dist라 지정
        dist,node =heapq.heappop(heap)
        
        #distances에 INF가 들어있기때문에 dist가 더크면 생략
        if distances[node] < dist:
            continue
        
        #graph배열에 인접한 노드와 비용을 가져온다
        for next_node,next_dist in graph[node]:
            #dist + next_dist를 distance에 저장
            distance = dist + next_dist
            #distance가 distances[next_node]보다 작으면
            #distance로 교체하고 heap에 push해준다.
            if distance<distances[next_node]:
                distances[next_node]=distance
                heapq.heappush(heap,[distance,next_node])
    #결과값을 distances를 넘겨줌
    return distances

    
if __name__=='__main__':
    
    N = int(s.readline())
    M = int(s.readline())
    graph = [[]for _ in range(N+1)]
    
    #graph[A]에 도착도시, 버스비용 저장
    for i in range(M):
        A,B,C = map(int,s.readline().split())
        graph[A].append((B,C))
    
    #출발, 도착지점 입력
    start, end  = map(int,s.readline().split())

    # INF(무한)의 값을 임의로 큰값을 넣어둠
    INF = int(1e9)
    
    
    #다익스르타 함수 호출 후 결과받아옴
    ans=dijkstra(graph,start)
    
    #출발지에서 도착지까지의 최소비용 
    print(ans[end])   