import java.util.*;
public class Solution {
    public boolean isInterleave(String s1, String s2, String s3) {
        int N1 = s1.length();
        int N2 = s2.length();

        if(s3.length() != N1 + N2 ){return false;}

        boolean[][] dp = new boolean[N1+1][N2+1];
        for(int i = 0; i < dp.length; i++){
            Arrays.fill(dp[i], false);
        }

        dp[0][0] = true;

        for(int i = 0; i < N1+1; i++){
            for(int j =0; j <N2+1; j++){
                if(i == 0 & j == 0){
                    continue;
                }
                if(j-1 >= 0 && dp[i][j-1] && s2.charAt(j-1) == s3.charAt(i+j-1)){
                    dp[i][j] = true;
                }else if(i-1 >= 0 && dp[i-1][j] && s1.charAt(i-1) == s3.charAt(i+j-1)){
                    dp[i][j] = true;
                }
            }
        }

        return dp[N1][N2];
    }

    public static void main(String[] argv){
        String s1 = "aabcc";
        String s2 = "dbbca";
        Solution s = new Solution();
        System.out.println(s.isInterleave(s1, s2, "aadbbcbcac"));
        System.out.println(s.isInterleave(s1, s2, "aadbbbaccc"));
    }
}
