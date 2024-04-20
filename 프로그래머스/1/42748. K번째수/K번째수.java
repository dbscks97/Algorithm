import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        
        for(int i=0; i<commands.length; i++){
            int start = commands[i][0] -1;
            int finish = commands[i][1] -1;
            int find = commands[i][2] -1;
            ArrayList<Integer> list = new ArrayList<>();
            
            for(int j=0; j<array.length; j++){
                if(j>=start && j<=finish){
                    list.add(array[j]);        
                }    
            }
            Collections.sort(list);
            int result = list.get(find);
            answer[i] = result;
        }
        return answer;
    }
}