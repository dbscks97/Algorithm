import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(br.readLine());
		int[][] array = new int[n][n];
		int[][] dp = new int[n][n];

		for (int i = 0; i < n; i++) {
			String[] input = br.readLine().split(" ");
			for (int j = 0; j < n; j++) {
				array[i][j] = Integer.parseInt(input[j]);
				dp[i][j] = 1;
			}
		}

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				for (int k = 0; k <= i; k++) {
					for (int l = 0; l <= j; l++) {
						if (array[k][l] < array[i][j]) {
							dp[i][j] = Math.max(dp[i][j], dp[k][l] + 1);
						}
					}
				}
			}
		}

		int longest = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				longest = Math.max(longest, dp[i][j]);
			}
		}

		System.out.println(longest);
	}
}
