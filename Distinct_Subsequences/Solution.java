import java.util.*;
public class Solution {
    public int myCount(int skip, String S, int s_i, String T, int t_i){
        System.out.println(String.format("s: %d, t: %d", s_i, t_i));

        if(skip > (S.length() - T.length())){return 0;}
        if(s_i == S.length() && t_i == T.length()) return 1;
        if(s_i == S.length() || t_i == T.length()) return 0;

        int count = 0 ;

        if(S.charAt(s_i) == T.charAt(t_i)){
            count += myCount(skip, S, s_i+1, T, t_i+1);
        }

        if(skip < (S.length()- T.length())){
            count += myCount(skip+1, S, s_i+1, T, t_i);
            count += myCount(skip+1, S, s_i, T, t_i+1);
        }
        return count;
    }

    int[][] buildMap(String S, String T){
        int N = T.length();
        int M = S.length();
        int[][] returnMap = new int[N][];
        // for(int i =0; i < N; i++){
        //     Arrays.fill(returnMap[i], S.length());
        // }

        int last_first_i = 0;
        for(int t_i = 0; t_i < T.length(); t_i++){
            ArrayList<Integer> location = new ArrayList<Integer>();
            char t = T.charAt(t_i);
            for(int s_i = last_first_i; s_i < S.length(); s_i++){
                if(t == S.charAt(s_i)){
                    location.add(s_i);
                }
            }

            returnMap[t_i] = new int[location.size()];

            for(int l_i = 0; l_i < location.size(); l_i++){
                returnMap[t_i][l_i] =location.get(l_i);
            }
            if(location.size() == 0){
                returnMap[t_i] = new int[1];
                returnMap[t_i][0] = S.length();
            }
            last_first_i = returnMap[t_i][0];
        }
        return returnMap;
    }

    int myCount2(int[][] t_map, String S, String T, int t_i, int t_m_i){
        int count =0 ;

        if(t_i == T.length()-1){return 1;}

        int current_pos = t_map[t_i][t_m_i];

        for(int tplus1_m_i = t_map[t_i+1].length-1; tplus1_m_i >= 0; tplus1_m_i--){
            if(t_map[t_i+1][tplus1_m_i] > current_pos ){
                count += myCount2(t_map, S, T, t_i+1, tplus1_m_i);
            }else{
                break;
            }
        }

        return count;
    }


    public int numDistinct(String S, String T) {
        int[][] count= new int[S.length()+1][T.length()+1];
        for(int i =0; i < count.length; i++){
            Arrays.fill(count[i], 0);
            count[i][0] = 1;
        }

        for(int s_i = 1; s_i <= S.length(); s_i++){
            for(int t_i = 1; t_i <= T.length(); t_i++){
                if(S.charAt(s_i-1) == T.charAt(t_i-1)){
                    count[s_i][t_i] = count[s_i-1][t_i] + count[s_i-1][t_i-1];
                }else{
                    count[s_i][t_i] = count[s_i-1][t_i];
                }
            }
        }
        return count[S.length()][T.length()];
    }


    public static void main(String[] argv){
        Solution s = new Solution();
        System.out.println(s.numDistinct("rabbbit", "rabbit"));
        System.out.println(s.numDistinct("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz", "rwmimatmhydhbujebqehjprarwfkoebcxxqfktayaaeheys"));
        System.out.println(s.numDistinct("ccc", "c"));
        System.out.println(s.numDistinct("", "c"));
        System.out.println(s.numDistinct("cccc", "c"));
        System.out.println(s.numDistinct("adbdadeecadeadeccaeaabdabdbcdabddddabcaaadbabaaedeeddeaeebcdeabcaaaeeaeeabcddcebddebeebedaecccbdcbcedbdaeaedcdebeecdaaedaacadbdccabddaddacdddc", "bcddceeeebecbc"));

    }
}
