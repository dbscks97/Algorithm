import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N + 1];
        int[] dp = new int[N + 1];

        // 계단 점수 입력
        for (int i = 1; i <= N; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        // N이 1 또는 2일 때 처리
        if (N == 1) {
            System.out.println(arr[1]);
            return;
        }
        if (N == 2) {
            System.out.println(arr[1] + arr[2]);
            return;
        }

        // 초기값 설정
        dp[1] = arr[1];
        dp[2] = arr[1] + arr[2];

        // DP 점화식
        for (int i = 3; i <= N; i++) {
            dp[i] = Math.max(dp[i - 2], dp[i - 3] + arr[i - 1]) + arr[i];
        }

        // 최댓값 출력
        System.out.println(dp[N]);
    }
}
