import java.util.*;

class Solution {
    public int solution(int[] order) {
        Stack<Integer> stack = new Stack<>(); 
        int num = 1;
        int index = 0;
        
        while (num <= order.length) {
            if (num == order[index]) {
                index++; 
            } else {
                stack.push(num);
            }
            num++; 
            
            
            while (!stack.isEmpty() && stack.peek() == order[index]) {
                stack.pop();
                index++; 
            }
        }
        
        return index;  
    }
}
