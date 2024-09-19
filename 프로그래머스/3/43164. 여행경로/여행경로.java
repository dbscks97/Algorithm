import java.util.*;

class Solution {
    String[] answer = {}; 
    boolean[] visited;
    boolean found;
    List<String> result = new ArrayList<>();
    
    public String[] solution(String[][] tickets) {
        visited = new boolean[tickets.length]; 
        Arrays.sort(tickets, Comparator.comparing((String[] ticket) -> ticket[0])
                                       .thenComparing(ticket -> ticket[1])); 
       
        for (int i = 0; i < tickets.length; i++) {
            if (tickets[i][0].equals("ICN")) {
                visited[i] = true;
                result.add("ICN");
                dfs(tickets[i][1], tickets, 1);
                if(found) break;
                visited[i] = false;
                result.remove(result.size()-1);
            }
        }
        
        return answer;
    }
    
    void dfs(String arrive, String[][] tickets, int count) {
        result.add(arrive); 
        
        if (count == tickets.length) {
            found = true;
            answer = result.toArray(new String[0]);
            return;
        }
        
        for (int i = 0; i < tickets.length; i++) {
            if (!visited[i] && tickets[i][0].equals(arrive)) {
                visited[i] = true;
                dfs(tickets[i][1], tickets, count + 1);
                if(found) return;
                visited[i] = false;
                
            }
        }
        result.remove(result.size() - 1);
    }
}
