class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 투 포인터
        nums = [[i,n] for i,n in enumerate(nums)]
        nums.sort(key= lambda x : x[1])

        left = 0
        right = len(nums)-1
        while left < right:
            if nums[left][1] + nums[right][1] == target:
                return [nums[left][0], nums[right][0]]
            elif nums[left][1] + nums[right][1] > target:
                right -= 1
            else:
                left += 1
        