import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int[][] arr;
	static Queue<int[]> queue;
	static int[] dx = {0, 1, 0, -1};
	static int[] dy = {1, 0, -1, 0};
	static int N, M;

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		arr = new int[M][N];
		queue = new ArrayDeque<>();

		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
				if (arr[i][j] == 1) {
					queue.add(new int[]{i, j});
				}
			}
		}

		System.out.println(bfs());
	}

	static int bfs() {
		int days = -1;
		while (!queue.isEmpty()) {
			int size = queue.size();
			for (int k = 0; k < size; k++) {
				int[] tomato = queue.poll();
				int x = tomato[0];
				int y = tomato[1];
				for (int i = 0; i < 4; i++) {
					int nx = x + dx[i];
					int ny = y + dy[i];

					if (0 <= nx && nx < M && 0 <= ny && ny < N && arr[nx][ny] == 0) {
						arr[nx][ny] = 1;
						queue.add(new int[]{nx, ny});
					}
				}
			}
			days++;
		}

		if (checkTomatoes()) {
			return days;
		} else {
			return -1;
		}
	}

	static boolean checkTomatoes() {
		for (int i = 0; i < M; i++) {
			for (int j = 0; j < N; j++) {
				if (arr[i][j] == 0) {
					return false;
				}
			}
		}
		return true;
	}
}
