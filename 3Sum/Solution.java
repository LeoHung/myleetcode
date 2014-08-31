import java.util.*;

public class Solution {
    public List<List<Integer>> threeSum(int[] num) {

        if(num.length < 3){return new ArrayList<List<Integer>>();}

        HashSet<List<Integer>> listSet = new HashSet<List<Integer>>();

        Arrays.sort(num);

        Map<Integer, Integer> num2count = new HashMap<Integer, Integer>();
        for(int n : num){
            if(num2count.containsKey(n)){
                num2count.put(n, num2count.get(n) +1);
            }else{
                num2count.put(n, 1);
            }
        }

        for(int i =0; i < num.length; i++){
            if(i -1 >=0 && num[i-1] == num[i]){
                 continue;
            }

            for(int j = i+1; j < num.length; j++){
                int n1 = num[i];
                int n2 = num[j];
                int sum2 = num[i] + num[j];
                if( -sum2 < n2 ){
                    continue;
                }
                if((num2count.containsKey(-sum2) && (-sum2 != n2)) ||
                    (-sum2 != n1 && -sum2 == n2 && num2count.get(-sum2) >= 2) ||
                    (-sum2 == n1 && -sum2 == n2 && num2count.get(-sum2) >= 3)
                    ){
                    List<Integer> list = new ArrayList<Integer>();
                    list.add(n1);
                    list.add(n2);
                    list.add(-sum2);
                    listSet.add(list);
                }
            }
        }

        List<List<Integer>> retList = new ArrayList<List<Integer>>(listSet);
        return retList;
    }
    public static void main(String[] argv){
        int[] data = new int[]{-1,0,1,0};
        Solution s = new Solution();
        System.out.println(s.threeSum(data));
    }
}
