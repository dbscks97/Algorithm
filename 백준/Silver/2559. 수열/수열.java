import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		int[] temperatures = new int[N];
        
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			temperatures[i] = Integer.parseInt(st.nextToken());
		}

		int sum = 0;
		for (int i = 0; i < K; i++) {
			sum += temperatures[i];
		}

		int maxSum = sum;

		for (int i = K; i < N; i++) {
			sum = sum - temperatures[i - K] + temperatures[i]; 
			maxSum = Math.max(maxSum, sum); 
		}

		System.out.println(maxSum);
	}
}
