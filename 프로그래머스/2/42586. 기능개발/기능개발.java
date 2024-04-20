import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        ArrayList<Integer> days = new ArrayList<>();
        
        for (int i = 0; i < progresses.length; i++) {
            int daysToComplete = (100 - progresses[i] + speeds[i] - 1) / speeds[i]; 
            days.add(daysToComplete);
        }

        ArrayList<Integer> result = new ArrayList<>();
        
        int maxDay = days.get(0);
        int count = 1;
        
        for (int i = 1; i < days.size(); i++) {
            if (days.get(i) <= maxDay) {
                count++; 
            } else {
                result.add(count);
                maxDay = days.get(i);
                count = 1;
            }
        }
        result.add(count); 
        
        int[] answer = new int[result.size()];
        for (int i = 0; i < result.size(); i++) {
            answer[i] = result.get(i);
        }

        return answer;
    }
}
