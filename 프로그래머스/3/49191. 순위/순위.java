import java.util.*;

class Solution {
    public int solution(int n, int[][] results) {
        int answer = 0;
        // 그래프 초기화 (승리: 1, 패배: -1, 알 수 없음: 0)
        int[][] graph = new int[n][n];
        
        for (int[] result : results) {
            int winner = result[0] - 1; // 인덱스를 0부터 시작
            int loser = result[1] - 1;
            graph[winner][loser] = 1;  // winner가 loser를 이김
            graph[loser][winner] = -1; // loser가 winner에게 짐
        }

        // 플로이드-와샬 알고리즘으로 간접 승패 관계 계산
        for (int k = 0; k < n; k++) { // 중간 노드
            for (int i = 0; i < n; i++) { // 출발 노드
                for (int j = 0; j < n; j++) { // 도착 노드
                    if (graph[i][k] == 1 && graph[k][j] == 1) {
                        graph[i][j] = 1; // i가 k를 이기고, k가 j를 이기면 i가 j를 이김
                        graph[j][i] = -1; // j는 i에게 짐
                    }
                }
            }
        }

        // 각 선수의 승패 관계를 확인
        for (int i = 0; i < n; i++) {
            int count = 0;
            for (int j = 0; j < n; j++) {
                if (graph[i][j] != 0) count++; // 승패 관계가 확정된 경우
            }
            if (count == n - 1) answer++; // 승패 관계가 모두 확정된 선수
        }

        return answer;
    }
}
