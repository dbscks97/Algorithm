import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.TreeMap;
import java.util.Map;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String line = br.readLine();

		Map<Character, Integer> word = new TreeMap<>();
		for (char c : line.toCharArray()) {
			word.put(c, word.getOrDefault(c, 0) + 1);
		}

		int oddCount = 0;
		char oddChar = '0';
		for (Map.Entry<Character, Integer> entry : word.entrySet()) {
			if (entry.getValue() % 2 == 1) {
				oddCount++;
				oddChar = entry.getKey();
			}
		}

		if (oddCount > 1) {
			System.out.println("I'm Sorry Hansoo");
			return;
		}

		StringBuilder firstHalf = new StringBuilder();
		StringBuilder secondHalf = new StringBuilder();

		for (Map.Entry<Character, Integer> entry : word.entrySet()) {
			char c = entry.getKey();
			int count = entry.getValue();

			for (int i = 0; i < count / 2; i++) {
				firstHalf.append(c);
			}
		}

		secondHalf.append(firstHalf).reverse();

		if(oddCount==1){
			firstHalf.append(oddChar);
		}


		System.out.println(firstHalf.toString()+secondHalf.toString());
	}
}
