import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> map = new HashMap<>();
        
        for (String people : participant) {
            map.put(people, map.getOrDefault(people, 0) +1);
        }
        
        for (String complet : completion) {
            map.put(complet, map.getOrDefault(complet, 0) -1);
        }
        
        for (Map.Entry<String, Integer> entry : map.entrySet()){
            if (entry.getValue() != 0){
                answer = entry.getKey();
            }
        }
        
        return answer;
    }
}