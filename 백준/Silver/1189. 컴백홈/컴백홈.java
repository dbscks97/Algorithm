import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static boolean[][] visited;
	static int R, C, K;
	static String[][] arr;
	static int[] dx = {-1, 0, 1, 0};
	static int[] dy = {0, 1, 0, -1};
	static int totalPaths = 0;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		visited = new boolean[R][C];
		arr = new String[R][C];

		for (int i = 0; i < R; i++) {
			String line = br.readLine();
			for (int j = 0; j < C; j++) {
				arr[i][j] = String.valueOf(line.charAt(j));
			}
		}

		visited[R - 1][0] = true;
		dfs(R-1,0, 1);
		System.out.println(totalPaths);

	}

	static void dfs(int x, int y, int count) {
		// x,y좌표가 오른쪽 맨위일 경우 카운트
		if(x == 0 && y == C-1){
			if(count == K){
				totalPaths++;
			}
		}

		for (int i = 0; i < 4; i++) {
			int nx = x+dx[i];
			int ny = y+dy[i];

			if (nx >= 0 && nx < R && ny >= 0 && ny < C && arr[nx][ny].equals(".") && !visited[nx][ny]) {
				visited[nx][ny] = true;
				dfs(nx, ny, count + 1);
				visited[nx][ny] = false;
			}
		}
	}
}
