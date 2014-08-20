public class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        // check if not possible
        int total_gas = 0;
        int total_cost = 0;
        int n = gas.length;
        for(int i=0; i < n; i++){
            total_gas += gas[i];
            total_cost += cost[i];
        }
        if(total_cost > total_gas){return -1;}

        // try for every mew i->i
        for( int i =0 ;i < n ; i++){
            int tmp = 0;
            boolean isOk = true;
            for( int k = 0 ; k < n ; k++){
                int j = (i + k) % n;
                tmp += (gas[j] - cost[j]);
                if (tmp < 0 ){
                    isOk = false;
                    break;
                }
            }
            if(isOk){
                return i;
            }
        }
        return -1;
    }
    public static void main(String[] argv){
        int[] gas = {1, 2 };
        int[] cost = {2, 1};

        Solution s = new Solution();

        System.out.println(s.canCompleteCircuit(gas, cost));

    }
}
