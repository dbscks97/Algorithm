import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());

		StringBuilder result = new StringBuilder();

		for (int i = 0; i < N; i++) {
			int M = Integer.parseInt(br.readLine());
			HashMap<String, Boolean> phoneMap = new HashMap<>();
			boolean isPrefixFree = true;

			for (int j = 0; j < M; j++) {
				String phoneNumber = br.readLine();
				phoneMap.put(phoneNumber, true);
			}

			// 접두어 체크
			for (String number : phoneMap.keySet()) {
				for (int j = 1; j < number.length(); j++) {
					if (phoneMap.containsKey(number.substring(0, j))) {
						isPrefixFree = false;
						break;
					}
				}
			}

			result.append(isPrefixFree ? "YES\n" : "NO\n");
		}

		System.out.print(result);
	}
}
