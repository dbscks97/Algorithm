import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int N = scanner.nextInt();
        int K = scanner.nextInt();

        int start = 1;
        long end = 100000000000L;

        while (start <= end) {
            long mid = (start + end) / 2;
            long result = 0;

            if (mid > (long) N * N) {
                end = mid - 1;
                continue;
            }

            for (int i = 1; i <= N; i++) {
                result += Math.min(mid / i, N);
            }

            if (result < K) {
                start = (int) mid + 1;
            } else {
                end = mid - 1;
            }
        }

        System.out.println(start);

        scanner.close();
    }
}