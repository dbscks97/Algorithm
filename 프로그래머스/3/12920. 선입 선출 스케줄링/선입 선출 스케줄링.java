import java.util.*;

class Solution {
    public long solution(long n, int[] cores) {
        // 코어의 수
        int coreCount = cores.length;

        // 작업의 수가 코어의 수 이하인 경우
        if (n <= coreCount) {
            return n; // 첫 n개의 작업은 각 코어에서 처리
        }

        // 이진 탐색을 위한 범위 설정
        long left = 0;
        long right = 10000L * 50000L; // 최대 작업 시간의 최댓값

        long time = 0; // 작업 완료까지 걸리는 최소 시간
        long completedJobs = 0; // time까지 완료된 작업 수

        // 이진 탐색 수행
        while (left <= right) {
            long mid = (left + right) / 2;
            long totalJobs = 0; // mid 시간까지 완료된 작업 수 계산

            for (int coreTime : cores) {
                totalJobs += mid / coreTime + 1; // 각 코어가 처리할 수 있는 작업 수
            }

            if (totalJobs >= n) { // 작업 수가 충분한 경우
                time = mid;
                right = mid - 1; // 더 작은 시간으로 탐색
            } else {
                left = mid + 1; // 더 큰 시간으로 탐색
            }
        }

        // time 시간까지 완료된 작업 수 확인
        completedJobs = 0;
        for (int coreTime : cores) {
            completedJobs += (time - 1) / coreTime + 1; // time-1까지 완료된 작업 수
        }

        // 남은 작업 분배
        long remainingJobs = n - completedJobs;

        // 마지막 작업을 처리하는 코어 찾기
        for (int i = 0; i < coreCount; i++) {
            if (time % cores[i] == 0) { // 현재 시간이 해당 코어의 작업 처리 시간 배수일 경우
                remainingJobs--;
                if (remainingJobs == 0) {
                    return i + 1; // 코어 번호 반환 (1부터 시작)
                }
            }
        }

        return -1;
    }
}
