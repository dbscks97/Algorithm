import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());

		for (int i = 0; i < T; i++) {
			String s = br.readLine();
			LinkedList<Character> myLinkedList = new LinkedList<>();

			boolean isBalanced = true;
			for (char c : s.toCharArray()) {
				if (c == '(') {
					myLinkedList.add(c);
				} else {
					if (myLinkedList.isEmpty()) {
						System.out.println("NO");
						isBalanced = false;
						break;
					} else {
						myLinkedList.poll();
					}
				}
			}
			if (isBalanced && myLinkedList.isEmpty()) {
				System.out.println("YES");
			} else if(isBalanced) {
				System.out.println("NO");
			}
		}
	}
}
