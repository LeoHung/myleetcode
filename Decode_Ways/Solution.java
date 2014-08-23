// import java.lang.*;
public class Solution {
    public int numDecodings(String s) {
        if(s.length() == 0){
            return 0;
        }

        int[] numD = new int[s.length()];

        for(int i =0; i < s.length(); i++){
            if(i==0){
                if(s.charAt(0) == '0'){
                    return 0;
                }else{
                    numD[i] = 1;
                }
            }else if(i == 1){
                if(s.charAt(i) == '0'){
                    if(s.charAt(i-1) != '0' && Integer.valueOf(s.substring(0,1+1)) <= 26){
                        numD[i] = 1;
                    }else{
                        return 0;
                    }
                }else{
                    if(s.charAt(i-1) != '0' && Integer.valueOf(s.substring(0,1+1)) <= 26 ){
                        numD[i] = 2;
                    }else{
                        numD[i] = 1;
                    }
                }
            }else{
                if(s.charAt(i) == '0'){
                    if(s.charAt(i-1) != '0' && Integer.valueOf(s.substring(i-1,i+1)) <= 26 ){
                        numD[i] = numD[i-2];
                    }else{
                        return 0;
                    }
                }else{
                    if(s.charAt(i-1) != '0' && Integer.valueOf(s.substring(i-1,i+1)) <= 26){
                        numD[i] = numD[i-1] + numD[i-2];
                    }else{
                        numD[i] = numD[i-1];
                    }
                }
            }
        }


        return numD[s.length()-1];
    }

    public static void main(String[] argv){
        Solution s = new Solution();
        System.out.println(s.numDecodings("101"));
        // System.out.println(s.numDecodings("12"));
        // System.out.println(s.numDecodings("10"));
    }
}
