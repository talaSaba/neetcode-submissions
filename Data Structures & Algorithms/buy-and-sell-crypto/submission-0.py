class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=1
        sell=0
        madx=0
        leng=len(prices)
        while sell<buy and buy<leng:
            now=prices[buy]-prices[sell]
            if now<0:
                sell+=1
                if buy==sell:
                    buy+=1
            else:
                if now>madx:
                    madx=now
                buy+=1    
        return madx            

