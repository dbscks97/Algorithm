import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int N, M;
	static int[][] graph;
	static int r, c, direction;
	static int[] dx = {-1, 0, 1, 0};
	static int[] dy = {0, 1, 0, -1};
	static int cleanedCount = 0;


	public static void main(String[] args) throws IOException {
		// BufferedReader br = new BufferedReader(new FileReader("src/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		graph = new int[N][M];

		st = new StringTokenizer(br.readLine());
		r = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
		direction = Integer.parseInt(st.nextToken());

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		simulate();
		System.out.println(cleanedCount);
	}

	static void simulate() {
		while (true) {
			if (graph[r][c] == 0) {
				graph[r][c] = 2;
				cleanedCount++;
			}

			boolean moved = false;

			for (int i = 0; i < 4; i++) {
				direction = (direction+3) % 4;
				int nx = r + dx[direction];
				int ny = c + dy[direction];

				if (nx >= 0 && nx < N && ny >= 0 && ny < M && graph[nx][ny] == 0) {
					r=nx;
					c=ny;
					moved=true;
					break;
				}
			}

			if (!moved) {
				int backDir = (direction + 2) % 4; // 후진 방향
				int bx = r + dx[backDir];
				int by = c + dy[backDir];

				// 후진 가능하면 후진
				if (bx >= 0 && bx < N && by >= 0 && by < M && graph[bx][by] != 1) {
					r = bx;
					c = by;
				} else {
					break;
				}
			}
		}
	}
}
