import java.util.*;
public class Solution {

    class Anchor{
        int min_pos;
        int max_pos;
    }

    public String minWindow(String S, String T) {
        Map<Character, Integer> char2index = new HashMap<Character, Integer>();

        int tmp_c_index=0;
        for(int i=0; i < T.length(); i++){
            if(char2index.containsKey(T.charAt(i))){continue;}
            char2index.put(T.charAt(i), tmp_c_index);
            tmp_c_index++;
        }

        int[][] can_min = new boolean[char2index.size()][S.length()];
        int[][] can_max = new boolean[char2index.size()][S.length()];

        for(int i = 0; i < can_min.length; i++){
            Arrays.fill(can_min[i], 0);
            Arrays.fill(can_max[i], 0);
        }


        for(int i = 0; i < S.length(); i++){
            Character c = S.charAt(i);
            Integer c_index = char2index.get(c);
            if(c_index != null){
                if(c_index == 0){
                    can_max[c_index][i] = 1;
                }else{
                    can_max[c_index][i] = can_max[c_index][i-1] +1;
                }
            }
            for(int j =0 ; j < can_max.length; j++){
                if(c_index != null && j == c_index ){continue;}
                if(i-1 >=0){
                    can_max[j][i] = can_max[j][i-1];
                }else{
                    can_max[j][i] = 0;
                }
            }
        }

        for(int i = S.length() - 1; i >= 0 ;i--){
            Character c = S.charAt(i);
            Integer c_index = char2index.get(c);
            if(c_index != null){
                can_min[c_index][i] = true;
            }
            for(int j=0; j < can_min.length; j++){
                if(c_index != null && j == c_index){continue;}
                if(i+1 < S.length()){
                    can_min[j][i] = can_min[j][i+1];
                }else{
                    can_min[j][i] = false;
                }
            }
        }

        int max_pos = -1;
        for(int i =0; i <S.length();i++){
            boolean can_max_i = true;
            for(int c_i = 0; c_i < can_max.length; c_i++){
                can_max_i = can_max_i && can_max[c_i][i];
            }
            if(can_max_i){
                max_pos = i;
            }
        }
        if(max_pos < 0){return "";}

        int min_pos = -1;
        for(int i=0; i < S.length(); i++){
            boolean can_min_i = true;
            for(int c_i = 0; c_i < can_min.length; c_i++){
                can_min_i = can_min_i && can_min[c_i][i];
            }
            if(can_min_i){
                min_pos = i;
            }
        }
        if(min_pos <0 ){return "";}

        return S.substring(min_pos, max_pos+1);

    }

    public static void main(String[] argv){
        String S = "ADOBECODEBANC";
        String T = "ABC";
        Solution s = new Solution();

        System.out.println(s.minWindow(S, T));
        System.out.println(s.minWindow("a", "aa"));
    }
}

