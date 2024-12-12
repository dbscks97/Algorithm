import java.util.*;

class Solution {
    public int solution(int n, int[][] edge) {
        int answer = 0;
        List<List<Integer>> graph = new ArrayList<>();
        
        for(int i=0; i<n+1; i++){
            graph.add(new ArrayList<>());
        }
        
        for(int[] vertex : edge){
            int a = vertex[0];
            int b = vertex[1];
            graph.get(a).add(b);
            graph.get(b).add(a);
        }
        
        Queue<Integer> q = new LinkedList<>();
        q.offer(1);
        int[] distances = new int[n+1];
        Arrays.fill(distances,1);
        
        boolean[] visited = new boolean[n + 1];
        visited[1] = true;
        
        while(!q.isEmpty()){
            int current = q.poll();
            
            for(int neighbor : graph.get(current)){
                if(!visited[neighbor]){
                    q.offer(neighbor);
                    visited[neighbor]=true;
                    distances[neighbor] = distances[current]+1;
                }
            }
        }
        
        int maxDist = 0;
        for(int i=0; i<distances.length; i++){
            if(distances[i] > maxDist){
                maxDist= distances[i];
            }
        }
        
        for(int ans : distances){
            if(ans == maxDist){
                answer++;
            }
            
        }
        
        return answer;
    }
}