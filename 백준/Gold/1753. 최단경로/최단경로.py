from sys import stdin as s
import heapq as hq

def dijkstra(start):
    global dis
    
    q = []
    hq.heappush(q,(0,start))
    dist[start]=0
    
    while q:
        distance, now = hq.heappop(q)
        if dist[now] < distance:
            continue
        
        for i in graph[now]:
            cost = distance + i[1]
            
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                hq.heappush(q,(cost,i[0]))


if __name__=="__main__":
    V,E = map(int,s.readline().split())
    K = int(s.readline())
    INF = int(1e9)
    dist = [INF] *(V+1)
    graph = [[]for _ in range(V+1)]

    for i in range(E):
        u,v,w = map(int,s.readline().split())
        graph[u].append((v,w))
    
    dijkstra(K)

    for i in range(1,V+1):
        if dist[i] == INF:
            print('INF')
        else:
            print(dist[i])