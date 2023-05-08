import java.io.IOException;
import java.io.InputStreamReader;
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader((System.in)));

        int x = Integer.parseInt(br.readLine());

        int dp[] = new int[x+1];
        int ans[] = new int[x+1];
        String str ="";
        dp[0] = dp[1] = 0;

        for(int i=2; i<=x; i++){
            dp[i] = dp[i-1]+1;
            ans[i] = i-1;

            if(i%2==0 && dp[i] >dp[i/2]+1){
                dp[i] = dp[i/2] +1;
                ans[i] = i/2;
            }
            if(i%3==0 && dp[i]>dp[i/3]+1){
                dp[i] = dp[i / 3]+1;
                ans[i] = i/3;
            }
        }

        System.out.println(dp[x]);

        while(x > 0){
            str += x + " ";
            x = ans[x];
        }

        System.out.print(str);
     }
}
