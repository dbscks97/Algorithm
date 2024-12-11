import java.util.*;

class Solution {
    public long solution(int n, int[] works) {
        long answer = 0;
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());

        for(int i=0; i<works.length; i++){
            maxHeap.offer(works[i]);
        }
        
        for(int i=0; i<n; i++){
            int num = maxHeap.poll();
            if(num == 0){
                break;
            }
            num -= 1;
            maxHeap.offer(num);
        }
        
        while (!maxHeap.isEmpty()) {
            int ans = maxHeap.poll();
            answer += (long) ans * ans; 
        }
        
        return answer;
    }
}
