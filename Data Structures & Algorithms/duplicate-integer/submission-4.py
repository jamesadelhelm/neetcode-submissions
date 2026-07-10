class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ourSet = set()
        
        for num in nums:
            if num in ourSet:
                
                return True
            else:
                ourSet.add(num)
        
        return False
    