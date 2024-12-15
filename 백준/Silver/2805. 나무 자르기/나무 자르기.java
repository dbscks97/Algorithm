import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());

		int[] tree = new int[N];
		int start = 0;
		int end = 0;
		int answer = 0;
			st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			tree[i] = Integer.parseInt(st.nextToken());
			if(end<tree[i]){
				end = tree[i];
			}
		}

		while (start <= end) {
			int mid = (start + end) / 2;
			long count = 0;

			for (int i = 0; i < tree.length; i++) {
				if((tree[i] - mid) >0){
					count += (tree[i]-mid);
				}
			}

			if(count>=M){
				start = mid+1;
				answer = mid;
			} else{
				end = mid-1;
			}
		}

		System.out.println(answer);
	}
}
