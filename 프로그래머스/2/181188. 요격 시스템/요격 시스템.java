import java.util.*;

class Solution {
    public int solution(int[][] targets) {
        int answer = 0;
        int last_start = 0;
        Arrays.sort(targets, Comparator.comparingInt((int[] target) -> target[1]));
        
        for(int[] target : targets){
            int start = target[0];
            int end = target[1];
    
            if(start >= last_start){
                answer++;
                last_start=end;
            }
            
        }

        return answer;
    }
}