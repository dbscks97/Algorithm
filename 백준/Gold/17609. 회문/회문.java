import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int num = Integer.parseInt(br.readLine());
		for(int i =0; i<num; i++){
			String input = br.readLine().trim();

			int result = checkPalindrome(input);
			System.out.println(result);
		}
	}
	public static int checkPalindrome(String str){
		if (isPalindrome(str)) {
			return 0;
		} else if (isAlmostPalindrome(str)) {
			return 1;
		} else {
			return 2;
		}
	}
	public static boolean isPalindrome(String str) {
		int left = 0;
		int right = str.length() - 1;

		while (left < right) {
			if (str.charAt(left) != str.charAt(right)) {
				return false;
			}
			left++;
			right--;
		}
		return true;
	}
	public static boolean isAlmostPalindrome(String str) {
		int left = 0;
		int right = str.length() - 1;

		while (left < right) {
			if (str.charAt(left) != str.charAt(right)) {
				return isPalindrome(str.substring(left + 1, right + 1)) ||
					isPalindrome(str.substring(left, right));
			}
			left++;
			right--;
		}
		return false;
	}
}
