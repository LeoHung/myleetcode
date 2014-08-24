import java.util.*;

public class Solution {

    class Step{
        String text;
        boolean isSep;
        public Step(String text){
            this.text = text;
            if(text == null){this.isSep = true;} else{ this.isSep = false;}
        }
    }
    public boolean canGo(String from, String to){
        int diff_count = 0;
        for(int i =0 ;i < from.length(); i++){
            if( from.charAt(i) != to.charAt(i) ){
                diff_count+=1;
            }
        }
        if(diff_count == 1){
            return true;
        }else{
            return false;
        }
    }

    public int ladderLength(String start, String end, Set<String> dict) {

        dict.add(end);

        Queue<Step> q = new LinkedList<Step>();

        Step sep = new Step(null);

        q.add(new Step(start));
        q.add(sep);

        int N = dict.size();

        int numOfSep = 0;
        while(q.peek() != null && numOfSep <= N){
            Step curStep = q.poll();
            if(curStep.isSep){
                numOfSep +=1;

                if(q.peek() != null){
                    q.add(sep);
                }else{
                    break;
                }
            }else{

                for(int i = 0 ; i < curStep.text.length(); i++){

                    char[] charArray = curStep.text.toCharArray();
                    for(char c = 'a'; c <= 'z'; c++){
                        charArray[i] = c;
                        String nextString = new String(charArray);

                        if(!dict.contains(nextString)){continue;}

                        if(nextString.compareTo(end) == 0){
                            return numOfSep + 2;
                        }else{
                            q.add(new Step(nextString));
                            dict.remove(nextString);
                        }
                    }
                }
            }
        }

        return 0;
    }

    public static void main(String[] argv){
        Solution s = new Solution();
        String start = "hit";
        String end = "cog";
        String[] dict_a = new String[]{"hot", "dot", "dog", "lot", "log"};
        Set<String> dict = new HashSet<String>();
        for(String d_w : dict_a){ dict.add(d_w);}

        // System.out.println(dict.contains(new String("dog")));

        System.out.println(s.ladderLength(start, end, dict));
    }


}
