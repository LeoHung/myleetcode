public class Solution {



    public int atoi(String str) {
        if( str == null) {
            return 0;
        }

        str = str.trim();
        if( str.length() ==0){
            return 0;
        }

        int signnum = 0;

        long res= 0;

        boolean pos = true ;
        for( int i =0;i < str.length(); i++){
            char c = str.charAt(i);

            if( c == '+'){
                pos = true;
                signnum +=1;
                if(signnum >1){return 0;}
                continue;
            }else if(c == '-'){
                pos = false;
                signnum +=1;
                if(signnum >1){return 0;}
                continue;
            }

            if( '0' <= c && c <= '9' ){
                res = res * 10 + (c - '0');
            }else{
                break;
            }
            if(res > (long) 2147483647){
                if(pos){
                    return 2147483647;
                }else{
                    return -2147483648;
                }
            }
        }

        if(pos) {
            return (int) res;
        }else{
            return (int) -res;
        }



    }
    public static void main(String[] argv ){
        Solution s = new Solution();
        System.out.println(s.atoi("11111"));
        System.out.println(s.atoi("1111111111111111111111111111111111111111111"));
        System.out.println(s.atoi("-111111aaa"));
        System.out.println(s.atoi("-1111111111111111111111111111111111111111111"));
    }
}
