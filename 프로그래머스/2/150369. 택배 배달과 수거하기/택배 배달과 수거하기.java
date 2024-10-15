class Solution {
    public long solution(int cap, int n, int[] deliveries, int[] pickups) {
        long totalDistance = 0;
        int deliveryRemain = 0;
        int pickupRemain = 0;

        for (int i = n - 1; i >= 0; i--) {
            int cnt =0;
            deliveryRemain += deliveries[i];
            pickupRemain += pickups[i];

            while (deliveryRemain > 0 || pickupRemain > 0) {
        
                deliveryRemain -= cap;
                pickupRemain -= cap;
                cnt++;
            }
            totalDistance += (i + 1) * 2 * cnt;
        }

        return totalDistance;
    }
}
