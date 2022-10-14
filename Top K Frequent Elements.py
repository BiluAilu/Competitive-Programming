class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        result=[]
        from collections import Counter
        dicts=Counter(nums)
        rsorted= sorted(dicts, key=dicts.get, reverse=True)
        return(rsorted[:k])
                
            
  

            
        
            
        