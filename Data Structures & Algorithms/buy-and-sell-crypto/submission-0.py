class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        curr_max = 0
        while l < r and r < len(prices):
            if prices[r] > prices[l]:
                temp_max = prices[r] - prices[l]
                if temp_max > curr_max:
                    curr_max = temp_max
            else:
                l=r
            r+=1
        return curr_max