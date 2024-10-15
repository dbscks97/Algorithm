import java.util.*;

class Solution {
    public String[] solution(String[] record) {
        List<String> answer = new LinkedList<>();
        HashMap<String, String> map = new HashMap<>();

        
        for (String entry : record) {
            String[] details = entry.split(" ");
            String action = details[0];
            String userId = details[1];

            if (action.equals("Enter") || action.equals("Change")) {
                String username = details[2];
                map.put(userId, username);
            }
        }
        
        for (String entry : record) {
            String[] details = entry.split(" ");
            String action = details[0];
            String userId = details[1];

            if (action.equals("Enter")) {
                answer.add(map.get(userId)+"님이 들어왔습니다.");
            }
            
            if (action.equals("Leave")) {
                answer.add(map.get(userId)+"님이 나갔습니다.");
            }
            
        }
         return answer.toArray(new String[answer.size()]);
    }
       
}