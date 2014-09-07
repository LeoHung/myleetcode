public class Solution {
    public int sqrt(int x) {
        long ans = 0;
        int bit = 1 << 16;
        while(bit > 0){
            ans |= bit;
            if(ans*ans > x){
                ans ^= bit;
            }
            bit >>=1;
        }
        return (int) ans;
    }

    public static void main(String[] argv){
        Solution s = new Solution();

        System.out.println(s.sqrt(1));
        System.out.println(s.sqrt(256));
        System.out.println(s.sqrt(5));
    }
}
