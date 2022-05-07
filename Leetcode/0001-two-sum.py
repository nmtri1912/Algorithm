class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for index, num in enumerate(nums):
            remaining = target - num
            if remaining in seen:
                return [index, seen[remaining]]
            seen[num] = index

        