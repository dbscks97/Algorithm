import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int answer = 0;
		int N = Integer.parseInt(br.readLine());
		int K = Integer.parseInt(br.readLine());

		int[] sensors = new int[N];

		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			int num = Integer.parseInt(st.nextToken());
			sensors[i] = num;
		}

		Arrays.sort(sensors);

		int[] distance = new int[N - 1];

		for (int i = 0; i < N - 1; i++) {
			int first = sensors[i];
			int second = sensors[i + 1];

			distance[i] = second - first;
		}

		Arrays.sort(distance);

		for(int i =0; i<N-K; i++){
			answer += distance[i];
		}

		System.out.println(answer);
	}
}
