import math
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        piles.sort()
        n = len(piles)
        index = math.floor(n/3) 
        result = 0
        while index < n:
            result += piles[index]
            index += 2
            
        return result