import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main {
	public static void main(String[] args) throws IOException {
		// BufferedReader br = new BufferedReader(new FileReader("src/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine()); // 테스트 케이스 수

		for (int t = 0; t < T; t++) {
			String W = br.readLine(); // 문자열 입력
			int K = Integer.parseInt(br.readLine()); // K 입력

			int minLength = Integer.MAX_VALUE;
			int maxLength = Integer.MIN_VALUE;

			// 각 문자의 등장 위치를 기록
			ArrayList<Integer>[] positions = new ArrayList[26];
			for (int i = 0; i < 26; i++) {
				positions[i] = new ArrayList<>();
			}

			for (int i = 0; i < W.length(); i++) {
				positions[W.charAt(i) - 'a'].add(i);
			}

			// 각 문자의 등장 위치에 대해 슬라이딩 윈도우 적용
			for (int i = 0; i < 26; i++) {
				if (positions[i].size() < K) continue; // K번 등장하지 않는 문자는 무시

				ArrayList<Integer> pos = positions[i];

				for (int j = 0; j <= pos.size() - K; j++) {
					int start = pos.get(j);
					int end = pos.get(j + K - 1);

					// 최소 길이
					minLength = Math.min(minLength, end - start + 1);

					// 최대 길이 (첫 글자와 마지막 글자가 동일)
					maxLength = Math.max(maxLength, end - start + 1);
				}
			}

			// 결과 출력
			if (minLength == Integer.MAX_VALUE || maxLength == Integer.MIN_VALUE) {
				System.out.println(-1);
			} else {
				System.out.println(minLength + " " + maxLength);
			}
		}
	}
}
