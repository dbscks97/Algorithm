import java.util.*;

class Solution {
    public int solution(String begin, String target, String[] words) {
        if (!Arrays.asList(words).contains(target)) {
            return 0;
        }

        Queue<String[]> queue = new LinkedList<>();
        boolean[] visited = new boolean[words.length];

        queue.add(new String[]{begin, "0"});

        while (!queue.isEmpty()) {
            String[] current = queue.poll();
            String currentWord = current[0];
            int currentStep = Integer.parseInt(current[1]);

            if (currentWord.equals(target)) {
                return currentStep;
            }
           
            for (int i = 0; i < words.length; i++) {
                if (!visited[i] && isOneLetterDiff(currentWord, words[i])) {
                    visited[i] = true;
                    queue.add(new String[]{words[i], String.valueOf(currentStep + 1)});
                }
            }
        }
        return 0; 
    }

    private boolean isOneLetterDiff(String word1, String word2) {
        int diffCount = 0;

        for (int i = 0; i < word1.length(); i++) {
            if (word1.charAt(i) != word2.charAt(i)) {
                diffCount++;
            }
            if (diffCount > 1) {
                return false;
            }
        }
        return diffCount == 1;
    }
}
