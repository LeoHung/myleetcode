class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if prices == None or  len(prices) <=1 : 
            return 0
            
        last_min_p = prices[0]
        last_p = prices[0]
        
        profit = 0
        
        for p in prices[1:]:
            if p < last_p:
                profit += (last_p - last_min_p)
                last_min_p = p 
            last_p = p
        
        if p > last_min_p:
            profit += (p - last_min_p)
        
        return profit
            
