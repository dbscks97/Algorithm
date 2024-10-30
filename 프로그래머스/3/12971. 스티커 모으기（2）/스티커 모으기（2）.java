class Solution {
    public int solution(int sticker[]) {
        int n = sticker.length;
        
        if(n == 1) {
            return sticker[0];
        }
        
        return Math.max(maxStickerSum(sticker, 0, n - 2), maxStickerSum(sticker, 1, n - 1));
    }
    
    public int maxStickerSum(int[] sticker, int start, int end){
        if(start == end){
            return sticker[start];
        }
        
        int[] dp = new int[end+1];
        
        dp[start] = sticker[start];
        dp[start+1] = Math.max(sticker[start], sticker[start+1]);
        
        for (int i = start + 2; i <= end; i++) {
            dp[i] = Math.max(dp[i - 1], dp[i - 2] + sticker[i]);
        }

        return dp[end];
    }
}