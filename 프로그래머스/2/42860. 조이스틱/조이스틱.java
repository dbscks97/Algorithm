class Solution {
    public int solution(String name) {
		int length = name.length();
		int answer = 0;
		int move = length - 1;  // 초기 커서 이동은 마지막 인덱스로 설정

		for (int i = 0; i < length; i++) {
			// 알파벳 변경 최솟값 계산
			char c = name.charAt(i);
			answer += Math.min(c - 'A', 'Z' - c + 1);

			int next = i + 1;
			while (next < length && name.charAt(next) == 'A') {
				next++;
			}

			move = Math.min(move, i + length - next + Math.min(i, length - next));
		}

		answer += move;
		return answer;
	}
}