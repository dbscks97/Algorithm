import java.util.*;

class Solution {
    public int[] solution(int rows, int columns, int[][] queries) {
        int[] answer = new int[queries.length];
        int[][] matrix = new int[rows][columns];
        
        int value = 1;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                matrix[i][j] = value++;
            }
        }

        for (int q = 0; q < queries.length; q++) {
            int x1 = queries[q][0] - 1;
            int y1 = queries[q][1] - 1;
            int x2 = queries[q][2] - 1;
            int y2 = queries[q][3] - 1;
            
            int temp = matrix[x1][y1];
            int minVal = temp;
            
            for (int i = x1; i < x2; i++) {
                matrix[i][y1] = matrix[i + 1][y1];
                minVal = Math.min(minVal, matrix[i][y1]);
            }
            
            for (int i = y1; i < y2; i++) {
                matrix[x2][i] = matrix[x2][i + 1];
                minVal = Math.min(minVal, matrix[x2][i]);
            }
            
            for (int i = x2; i > x1; i--) {
                matrix[i][y2] = matrix[i - 1][y2];
                minVal = Math.min(minVal, matrix[i][y2]);
            }
            
            for (int i = y2; i > y1; i--) {
                matrix[x1][i] = matrix[x1][i - 1];
                minVal = Math.min(minVal, matrix[x1][i]);
            }
            
            matrix[x1][y1 + 1] = temp;
            
            answer[q] = minVal;
        }

        return answer;
    }
}
