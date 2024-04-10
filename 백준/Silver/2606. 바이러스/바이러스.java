import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Deque;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	static int N,M;
	static boolean[] visited;
	static List<Integer>[] graph;
	static StringBuilder sb = new StringBuilder();
	static int visitedCount = 0;

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		N = Integer.parseInt(br.readLine());
		M = Integer.parseInt(br.readLine());
		visited = new boolean[N+1];
		graph = new ArrayList[N+1];

		for (int i = 1; i <= N; i++) {
			graph[i] = new ArrayList<Integer>();
		}


		for (int i = 0; i < M ; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());

			graph[a].add(b);
			graph[b].add(a);
		}

		for (int i = 1; i < N; i++) {
			Collections.sort(graph[i]);
		}

		bfs(1);
		System.out.println(visitedCount - 1);
	}

	static void bfs(int start) {
		Deque<Integer> queue = new ArrayDeque<>();
		queue.add(start);
		visited[start] = true;
		visitedCount++;

		while (!queue.isEmpty()) {
			int now = queue.poll();

			for (int next : graph[now]) {
				if (!visited[next]) {
					queue.add(next);
					visited[next]= true;
					visitedCount++;
				}
			}
		}
	}
}
