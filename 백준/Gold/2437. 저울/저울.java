import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
	public static void main(String[] args) throws IOException {
		// BufferedReader br = new BufferedReader(new FileReader("src/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(br.readLine());
		int[] weights = new int[n];

		String[] input = br.readLine().split(" ");
		for (int i = 0; i < n; i++) {
			weights[i] = Integer.parseInt(input[i]);
		}

		Arrays.sort(weights);

		int target = 1;

		for (int weight : weights) {
			if (weight > target) {
				break;
			}
			target += weight;
		}

		System.out.println(target);
	}
}
