class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # dict where nums value is key and that index is the val
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            else:
                seen[num] = i
        