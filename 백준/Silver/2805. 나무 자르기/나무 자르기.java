import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken()); // 나무의 수
        int M = Integer.parseInt(st.nextToken()); // 필요한 나무의 길이

        int[] tree = new int[N];
        int start = 0;
        int end = 0;

        // 나무 높이 입력 및 최대 높이 찾기
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            tree[i] = Integer.parseInt(st.nextToken());
            end = Math.max(end, tree[i]); // 가장 긴 나무 높이 찾기
        }

        int answer = 0;

        // 이분 탐색 시작
        while (start <= end) {
            int mid = (start + end) / 2; // 절단기의 높이
            long total = 0; // 잘린 나무 길이 합 (int로 부족할 수 있으므로 long 사용)

            // 나무를 자르고 총 길이 계산
            for (int i = 0; i < N; i++) {
                if (tree[i] > mid) {
                    total += (tree[i] - mid);
                }
            }

            // 필요한 나무 길이보다 많이 잘린 경우
            if (total >= M) {
                answer = mid; // 가능한 절단기 높이 저장
                start = mid + 1; // 더 높은 절단기 높이 탐색
            } else {
                end = mid - 1; // 절단기 높이를 낮춰야 함
            }
        }

        System.out.println(answer);
    }
}
