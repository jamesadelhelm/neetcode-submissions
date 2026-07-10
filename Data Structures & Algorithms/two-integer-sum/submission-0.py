class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        ourHashMap = {}

        for i, num in enumerate(nums):
            if (target - num) in ourHashMap:
                return [ourHashMap[target-num], i]
            ourHashMap[num] = i