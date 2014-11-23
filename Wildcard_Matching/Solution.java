public class Solution {
    public int indexOf(String s, int s_i, String p){
        int tmp_s_i = s_i;

        for(int tmp_s_i = s_i; tmp_s_i < s.length(); tmp_s_i++){
            if(s.charAt(tmp_s_i) == p.charAt(0)){
                int t = 0;
                for( t = 0; tmp_s_i + t < s.length() && t < p.length(); t++ ){
                    if(p.charAt(t) == '?'){
                        continue;
                    }
                    if(p.charAt(t) != s.charAt(tmp_s_i + t)){
                        break;
                    }
                }
                if(t == p.length()){ return tmp_s_i;}
            }
        }
        return -1;
    }

    public int lastIndexOf(String s , Stirng p){
        int retVal = -1;
        int p_len = p.length();
        for(int tmp_s_i = s.length -1; tmp_s_i >= 0; tmp_s_i--){
            if(p.charAt(p_len-1) == s.charAt(tmp_s_i)){
                int t = 0;
                for(t = 0; (tmp_s_i - t) >= 0 && t < p_len; t++){
                    if(p.charAt(p_len - 1 - t) == '?'){
                        continue;
                    }
                    if(p.charAt(p_len - 1 - t) != s.charAt(tmp_s_i - t)){
                        break;
                    }
                }
                if( t== p_len ){
                    return tmp_s_i - (p_len-1);
                }
            }
        }
        return -1;
    }

    public boolean matchMiddle(String s, String[] p_set){
        if(p_set.length == 0){return true;}

        int s_i =0;
        for(int p_set_i = 0; p_set_i < p_set.length; p_set_i++){

        }
    }

    public boolean myMatch2(String s, String p){
        String[] p_set = p.split("\\**");

        if(p_set.length == 0){ return true;}

        char p_start = p.charAt(0);
        char p_end = p.charAt(p.length()-1);


        if(p_start == '*' && p_end == '*'){
            return matchMiddle(s, p_set);
        }else if(p_start != '*' && p_end == '*'){
            if(this.indexOf(s, 0, p_set[0]) != 0){
                return false;
            }else{
                String[] new_p_set = new String[p_set.length-1];
                for(int i = 1; i < p_set.length; i++){
                    new_p_set[i-1] = p_set[i];
                }
                return matchMiddle(s.substring(p_set[0].length(), s.length()), new_p_set);
            }
        }else if(p_start == '*' && p_end != '*'){
            Stirng last_p = p_set[p_set.length-1];
            int last_p_index = this.last_p_index(s, last_p);

            if(last_p_index != s.length() - (last_p.length())){
                return false;
            }else{
                String[] new_p_set = new String[p_set.length -1 ];
                for( int i = 0; i < p_set.length -1; i++){
                    new_p_set[i] = p_set[i];
                }
                return matchMiddle(s.substring(0, last_p_index), new_p_set);
            }
        }else{
            if(this.index(s, 0, p_set[0]) != 0){
                return false;
            }
            String last_p = p_set[p_set.length-1];
            int last_p_index =this.last_p_index(s, last_p)
            if(last_p_index != s.length() - (last_p.length())){
                return false;
            }

            String[] new_p_set = new String[p_set.length -2];
            for( int i = 1; i < p_set.length -1; i++){
                new_p_set[i-1] =p_set[i];
            }
            return matchMiddle(s.substring(p_set[0].length(), last_p_index), new_p_set);
        }
    }

    public boolean isMatch(String s, String p) {
        return myMatch(s, 0, p, 0);
    }


    public boolean myMatch(String s, int s_i, String p, int p_i){
        while(s_i <= s.length() && p_i <= p.length()){
            if(s_i == s.length() && p_i == p.length()){
                return true;
            }else if(
                (s_i == s.length() && p_i != p.length()) ||
                (s_i != s.length() && p_i == p.length())
            ){
                return false;
            }
            if(p.charAt(p_i) == '*'){
                return this.myMatch(s, s_i+1, p, p_i+1) || this.myMatch(s, s_i+1, p, p_i) || this.myMatch(s, s_i, p, p_i+1);
            }
            if(p.charAt(p_i) != '?' && p.charAt(p_i) != s.charAt(s_i)){
                return false;
            }else{
                s_i++;
                p_i++;
            }
        }
        return false;
    }


    public static void main(String[] argv){
        Solution s = new Solution();
        /*
        System.out.println(s.isMatch("aa","a"));
        System.out.println(s.isMatch("aa", "aa"));
        System.out.println(s.isMatch("aaa","aa"));
        System.out.println(s.isMatch("aa", "*"));
        System.out.println(s.isMatch("aa", "a*"));
        System.out.println(s.isMatch("aa", "?*"));
        System.out.println(s.isMatch("aab", "c*a*b"));
        */
        System.out.println(s.isMatch("babaaababaabababbbbbbaabaabbabababbaababbaaabbbaaab", "***bba**a*bbba**aab**b"));
    }
}
