class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=0
        total=0
        for sell in range(1,len(prices)):
            if prices[buy]>prices[sell]:
                buy=sell
            elif prices[buy]<prices[sell]:
                total+=prices[sell]-prices[buy] 
                buy=sell
        return total        


        