import java.util.*;



public class Solution {
    Map<Integer, Set<Anchor>> pos2anchor;

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

    public List<List<String>> partition(String s) {
        // prepare for anchor
        this.pos2anchor = new HashMap<Integer, Set<Anchor>>();
        for(int i =0; i < s.length(); i++){
            for(int k =i+1; k <=s.length(); k++){
                String sub_s = s.substring(i, k);
                if(isPall(sub_s)){
                    if(!this.pos2anchor.containsKey(i)){
                        this.pos2anchor.put(i, new HashSet<Anchor>());
                    }
                    Anchor a = new Anchor();
                    a.text = sub_s;
                    a.start_pos = i ;
                    this.pos2anchor.get(i).add(a);
                }
            }
        }
        // print all possible combinations
        List<List<String>> ans = new ArrayList<List<String>>();

        List<String> tmp = new ArrayList<String>();
        Stack<Anchor> stack = new Stack<Anchor>();
        for(Anchor a : pos2anchor.get(0)){
            stack.push(a);
        }
        Anchor sep = new Anchor();
        sep.isSep = true;

        int current_pos = 0;
        while(stack.size() > 0){
            Anchor a = stack.pop();
            if(a.isSep){
                String removed_s = tmp.remove(tmp.size()-1);
                current_pos -= removed_s.length();
            }else{
                tmp.add(a.text);
                int len = a.text.length();

                if(current_pos + len == s.length()){
                    // copy this list to answers
                    ans.add(new ArrayList(tmp));
                }
                if(pos2anchor.containsKey(current_pos + len)){
                    current_pos += len;
                    stack.push(sep);
                    for(Anchor next_a : pos2anchor.get(current_pos)){
                        stack.push(next_a);
                    }
                }else{
                    //remove itself
                    tmp.remove(tmp.size()-1);
                }
            }
        }

        return ans;
    }
    public static void main(String[] argv){
        Solution s = new Solution();
        System.out.println(s.partition("aab"));
    }
}
