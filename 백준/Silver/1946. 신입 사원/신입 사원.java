import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int T = Integer.parseInt(br.readLine());

		for (int i = 0; i < T; i++) {
			int N = Integer.parseInt(br.readLine());
			List<int[]> arr = new ArrayList<>();

			for (int j = 0; j < N; j++) {
				String[] rank = br.readLine().split(" ");
				int docRank = Integer.parseInt(rank[0]);
				int intRank = Integer.parseInt(rank[1]);
				arr.add(new int[] {docRank, intRank});
			}

			arr.sort((a, b) -> Integer.compare(a[0], b[0]));

			int count = 0;
			int minIntRank = Integer.MAX_VALUE;
			for (int[] d : arr) {
				if (minIntRank > d[1]) {
					minIntRank = d[1];
					count++;
				}
			}

			System.out.println(count);
		}
	}
}
