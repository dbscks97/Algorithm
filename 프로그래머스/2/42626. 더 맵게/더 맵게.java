import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> queue = new PriorityQueue<>();
        
        for(int sco : scoville){
            queue.offer(sco);
        }
        
        while(queue.size() > 1 && queue.peek() < K){
            int first_scoville = queue.poll();
            int second_scoville = queue.poll();
            
            queue.offer(first_scoville + second_scoville * 2);
            answer++;
        }
        
         if (queue.peek() < K) {
            return -1;
        }
        
        return answer;
    }
}