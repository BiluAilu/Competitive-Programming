class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        days = 0
        n = len(prices)
        i = 0
        while i < len(prices):
            j = i
            while j < len(prices) - 1 and prices[j + 1] + 1 == prices[j]:
                j += 1
            days += (j - i) * (j - i + 1) // 2
            i = j + 1
            
        days += len(prices)
        return days
                
        
        