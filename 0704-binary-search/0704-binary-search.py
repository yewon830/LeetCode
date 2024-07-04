from bisect import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:   
        result = bisect_left(nums,target)
        if result<len(nums) and nums[result] == target:
            return result
        else:
            return -1