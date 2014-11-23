import java.util.*;
public class Solution {

    String longest = "";
    boolean[][] isPalindrome;

    public void setIsPalindromeTrue(int i, int j, String s){
        isPalindrome[i][j] = true;
        if(j-i+1 > longest.length()){
            longest = s.substring(i, j+1);
        }
    }

    public String longestPalindrome(String s) {
        int N = s.length();
        isPalindrome = new boolean[N][N];
        longest = "";

        for(int i = 0; i < N; i++){
            Arrays.fill(isPalindrome[i], false);
        }

        for(int t=0; t < s.length(); t++){
            for(int i =0; i < s.length(); i++){
                int j = i+t;
                if(j >= s.length()){break;}

                if(i ==j){
                    setIsPalindromeTrue(i, j, s);
                }else if( t==1 && s.charAt(i) == s.charAt(j)){
                    setIsPalindromeTrue(i, j, s);
                }else if( t >1 && s.charAt(i) == s.charAt(j) && isPalindrome[i+1][j-1]){
                    setIsPalindromeTrue(i, j, s);
                }
            }
        }
        return longest;
    }

    public static void main(String[] argv){
        Solution s = new Solution();
        System.out.println(s.longestPalindrome("abcbadd"));
        System.out.println(s.longestPalindrome("aaaaaaaa"));
    }
}
