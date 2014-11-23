class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if prices == None or len(prices) < 2 :
            return 0

        forward_max_profit = []
        last_min = prices[0]
        last_max_profit = 0

        for p in prices:
            if p - last_min > last_max_profit:
                last_max_profit = p - last_min
            if p < last_min: 
                last_min = p
            forward_max_profit.append(last_max_profit)
        
        print forward_max_profit 

        backward_max_profit = {}
        last_max = prices[-1]
        last_max_profit = 0
        
        for i in xrange(len(prices)-1, 0-1, -1):
            p = prices[i]
            if last_max - p > last_max_profit:
                last_max_profit = last_max - p 
            if p > last_max:
                last_max = p 
            backward_max_profit[i] = last_max_profit
        
        print backward_max_profit

        max_profit = backward_max_profit[0]
        for i in xrange(len(prices)):
            if i < len(prices) -1:
                profit = forward_max_profit[i] + backward_max_profit[i+1]
            else:
                profit = forward_max_profit[i]
            
            if profit > max_profit:
                max_profit = profit
                
        return max_profit
            
if __name__ == "__main__":
    s = Solution()
    #print s.maxProfit([2,1,2,0,1] )
