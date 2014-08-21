import java.util.*;

public class Solution {
    Map<Integer, ArrayList<Anchor>> pos2anchor;

    class Anchor{
        boolean isSep;
        int start_pos;
        String text;
        public Anchor(){
            isSep = false;
        }
    }
    public static boolean isPall(String s){
        for(int i= 0 ;i < (s.length()/2) ;i++){
            if(s.charAt(i) != s.charAt(s.length()-1-i)){
                return false;
            }
        }
        return true;
    }

    public int minCut(String s) {
        // prepare for anchor
        this.pos2anchor = new HashMap<Integer, ArrayList<Anchor>>();
        for(int i =0; i < s.length(); i++){
            for(int k =i+1; k <=s.length(); k++){
                String sub_s = s.substring(i, k);
                if(isPall(sub_s)){
                    if(!this.pos2anchor.containsKey(i)){
                        this.pos2anchor.put(i, new ArrayList<Anchor>());
                    }
                    Anchor a = new Anchor();
                    a.text = sub_s;
                    a.start_pos = i ;
                    this.pos2anchor.get(i).add(a);
                }
            }
            if(this.pos2anchor.containsKey(i)){
                Collections.sort(this.pos2anchor.get(i), new Comparator(){
                    public int compare(Object o1, Object o2){
                        Anchor a1 = (Anchor) o1;
                        Anchor a2 = (Anchor) o2;
                        return a2.text.length() - a1.text.length();
                    }
                });
            }
        }

        // find min cut
        int min = s.length()-1;

        Stack<Anchor> stack = new Stack<Anchor>();
        for(Anchor a : pos2anchor.get(0)){
            stack.push(a);
        }
        Anchor sep = new Anchor();
        sep.isSep = true;

        int current_seg = 0;
        while(stack.size() > 0){
            Anchor a = stack.pop();
            if(a.isSep){
                current_seg -= 1;
            }else{
                int len = a.text.length();
                int next_pos = a.start_pos + len;
                if(next_pos == s.length()){
                    if(current_seg + 1 -1 < min){
                        min = current_seg +1 -1;
                    }
                }
                if(pos2anchor.containsKey(next_pos) && current_seg < min){
                    current_seg += 1;
                    stack.push(sep);
                    for(Anchor next_a : pos2anchor.get(next_pos)){
                        stack.push(next_a);
                    }
                }
            }
        }

        return min;
    }

    public static void main(String[] argv){
        Solution s = new Solution();
        System.out.println(s.minCut("fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbhafehieabbdfeigbiaggchaeghaijfbjhi"));
    }
}
