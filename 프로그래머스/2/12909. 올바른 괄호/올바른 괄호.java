import java.util.Stack;

class Solution {
    boolean solution(String s) {
        Stack<Character> stack = new Stack<>();
        Boolean answer = true;
        
        for (char c : s.toCharArray()) {
            if (c == '(') {
                stack.push(c);
            } else { 
                if (!stack.isEmpty()) {
                    stack.pop();
                } else {
                    return false; 
                }
            }
        }
        if(!stack.isEmpty()){
            return false;
        }
        return answer;
    }
}
