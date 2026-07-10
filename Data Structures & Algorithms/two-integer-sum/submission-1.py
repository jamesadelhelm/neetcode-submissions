class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenHM = {}

        for currentIndex, currentNum in enumerate(nums):
            complement = target - currentNum
            if complement in seenHM:
                return [seenHM[complement], currentIndex]
            else:
                seenHM[currentNum] = currentIndex

        