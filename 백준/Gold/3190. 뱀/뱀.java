import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Deque;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int[][] board;
	static Map<Integer, String> directionMap = new HashMap<>();
	static int[] dx = {0, 1, 0, -1};
	static int[] dy = {1, 0, -1, 0};
	public static void main(String[] args) throws IOException {

		// BufferedReader br = new BufferedReader(new FileReader("src/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		int K = Integer.parseInt(br.readLine());
		board = new int[N][N];

		for (int i = 0; i < K; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken()) - 1;
			int y = Integer.parseInt(st.nextToken()) - 1;
			board[x][y] = 1;
		}

		int L = Integer.parseInt(br.readLine());
		for (int i = 0; i < L; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int time = Integer.parseInt(st.nextToken());
			String direction = st.nextToken();
			directionMap.put(time, direction);
		}
		System.out.println(simulate());
	}

	static int simulate() {
		Deque<int[]> snake = new LinkedList<>();
		snake.add(new int[] {0, 0});
		int time=0, direction=0;

		while (!snake.isEmpty()) {
			time++;
			int[] head = snake.peekLast();
			int nx = head[0] + dx[direction];
			int ny = head[1] + dy[direction];

			if (nx < 0 || nx >=N || ny < 0 || ny >=N || contains(snake, nx, ny)) {
				break;
			}

			if (board[nx][ny] == 1) {
				board[nx][ny] = 0;
			} else {
				snake.pollFirst();
			}

			snake.addLast(new int[] {nx, ny});

			if (directionMap.containsKey(time)) {
				direction = changeDirection(direction, directionMap.get(time));
			}
		}
		return time;
	}

	static int changeDirection(int X, String C) {
		if (C.equals("L")) {
			return(X+3)%4;
		} else {
			return(X+1)%4;
		}
	}

	static boolean contains(Deque<int[]> snake, int nx, int ny) {
		for (int[] part : snake) {
			if (part[0] == nx && part[1] == ny) {
				return true;
			}
		}
		return false;
	}
}
