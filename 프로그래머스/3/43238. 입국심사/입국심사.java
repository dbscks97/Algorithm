class Solution {
    public long solution(int n, int[] times) {
        long answer = Long.MAX_VALUE; // 최적 해를 저장
        long timeMax = 0;

        // 가장 느린 심사관의 처리 시간 찾기
        for (int time : times) {
            if (time > timeMax) {
                timeMax = time;
            }
        }

        // 이분 탐색 범위 설정
        long start = 1; // 최소 시간
        long end = timeMax * (long) n; // 최대 시간

        while (start <= end) {
            long mid = (start + end) / 2;
            long total = 0;

            // 현재 시간 `mid`에서 처리 가능한 사람 수 계산
            for (int time : times) {
                total += (mid / time);
                if (total >= n) { // 필요 인원 이상 처리 가능하면 조기 종료
                    break;
                }
            }

            if (total < n) { // 처리 가능한 인원이 부족하면 시간 증가
                start = mid + 1;
            } else { // 처리 가능하면 시간 줄이고 최적값 갱신
                answer = mid;
                end = mid - 1;
            }
        }

        return answer;
    }
}
