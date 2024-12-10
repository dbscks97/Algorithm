import java.util.*;

class Solution {
    public int solution(int[][] routes) {
        int answer = 0;
        int count = Integer.MIN_VALUE;
        Arrays.sort(routes, (a,b)-> Integer.compare(a[1], b[1]));
        
        for(int[] route : routes){
            int first = route[0];
            int second = route[1];
            
            if(first>count){
                count = second;
                answer+=1;
            }
        }
        
        return answer;
    }
}