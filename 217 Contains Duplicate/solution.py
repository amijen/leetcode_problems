class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        d = set(nums)
        if len(d) == len(nums):
            return False
        return True