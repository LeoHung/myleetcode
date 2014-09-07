import java.util.*;
public class Solution {
    public int lengthOfLongestSubstring(String s) {
        int b=0;
        int f=0;
        int max_len=0;
        HashSet<Character> seenChar = new HashSet<Character>();

        for( f=0; f< s.length(); f++){
            // System.out.println("f:"+f);
            if(!seenChar.contains(s.charAt(f))){
                seenChar.add(s.charAt(f));
                max_len = Math.max(max_len, (f-b +1));
            }else{
                while(seenChar.contains(s.charAt(f))){
                    seenChar.remove(s.charAt(b));
                    b++;
                    // System.out.println("b:"+b);
                }
                seenChar.add(s.charAt(f));
            }
        }

        return max_len;
    }
    public static void main(String[] argv){
        Solution s = new Solution();
        System.out.println(s.lengthOfLongestSubstring("bbbbbb"));
        System.out.println(s.lengthOfLongestSubstring("abcabcbb"));
    }
}
