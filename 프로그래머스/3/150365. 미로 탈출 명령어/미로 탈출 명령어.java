class Solution {
    // 방향 정의 (하, 좌, 우, 상) -> 사전순으로 탐색
    static int[] dx = {1, 0, 0, -1};
    static int[] dy = {0, -1, 1, 0};
    static String[] directions = {"d", "l", "r", "u"};

    public String solution(int n, int m, int x, int y, int r, int c, int k) {
        // 목표까지의 최단 거리 계산
        int distance = Math.abs(r - x) + Math.abs(c - y);
        
        // 이동할 수 없는 경우 처리
        if (distance > k || (k - distance) % 2 != 0) {
            return "impossible";
        }

        // 최적의 경로 탐색 (그리디)
        StringBuilder path = new StringBuilder();
        while (k > 0) {
            boolean moved = false;

            // 네 방향을 사전순으로 탐색
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                // 새로운 좌표가 미로 범위 내에 있는지 확인
                if (nx > 0 && nx <= n && ny > 0 && ny <= m) {
                    // 남은 거리 계산
                    int remainingDistance = Math.abs(r - nx) + Math.abs(c - ny);

                    // 남은 이동 횟수로 목표까지 도달할 수 있는지 확인
                    if (remainingDistance <= k - 1) {
                        path.append(directions[i]); // 경로 추가
                        x = nx;
                        y = ny;
                        k--; // 이동 횟수 감소
                        moved = true;
                        break; // 한번 이동하면 더 이상 다른 방향 탐색하지 않음
                    }
                }
            }

            // 이동할 수 없다면 불가능 처리
            if (!moved) {
                return "impossible";
            }
        }

        return path.toString();
    }
}
