import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken()); // 장애물 개수
        int H = Integer.parseInt(st.nextToken()); // 동굴 높이

        int[] bottom = new int[H + 1]; // 석순 (바닥에서 올라오는 장애물)
        int[] top = new int[H + 1]; // 종유석 (천장에서 내려오는 장애물)

        // 입력 처리
        for (int i = 0; i < N; i++) {
            int height = Integer.parseInt(br.readLine());
            if (i % 2 == 0) {
                bottom[height]++;
            } else {
                top[height]++;
            }
        }

        // 누적 합 계산 (높이별 장애물 개수)
        for (int i = H - 1; i >= 1; i--) {
            bottom[i] += bottom[i + 1];
            top[i] += top[i + 1];
        }

        int minObstacles = Integer.MAX_VALUE; // 최소 파괴 장애물 개수
        int count = 0; // 최소 개수가 나타나는 높이의 개수

        // 각 높이에서 파괴해야 하는 장애물 계산
        for (int i = 1; i <= H; i++) {
            int obstacles = bottom[i] + top[H - i + 1];
            if (obstacles < minObstacles) {
                minObstacles = obstacles;
                count = 1;
            } else if (obstacles == minObstacles) {
                count++;
            }
        }

        // 결과 출력
        System.out.println(minObstacles + " " + count);
    }
}
