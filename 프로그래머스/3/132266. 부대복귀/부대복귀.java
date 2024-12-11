import java.util.*;

class Solution {
    public int[] solution(int n, int[][] roads, int[] sources, int destination) {
        // 결과를 저장할 배열
        int[] answer = new int[sources.length];
        
        // 그래프 초기화
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }
        
        // 그래프 간선 정보 추가
        for (int[] road : roads) {
            int a = road[0];
            int b = road[1];
            graph.get(a).add(b);
            graph.get(b).add(a);
        }
        
        // 최단 거리를 저장할 배열
        int[] distances = new int[n + 1];
        Arrays.fill(distances, -1); // 초기값 -1로 설정
        
        // BFS로 최단 거리 계산
        Queue<Integer> queue = new LinkedList<>();
        queue.add(destination);
        distances[destination] = 0; // 시작 지점의 거리는 0
        
        while (!queue.isEmpty()) {
            int current = queue.poll();
            for (int neighbor : graph.get(current)) {
                if (distances[neighbor] == -1) { // 아직 방문하지 않은 노드
                    distances[neighbor] = distances[current] + 1;
                    queue.offer(neighbor);
                }
            }
        }
        
        // sources 배열을 기반으로 결과 구성
        for (int i = 0; i < sources.length; i++) {
            answer[i] = distances[sources[i]]; // 도달 불가능하면 -1로 유지
        }
        
        return answer;
    }
}
