class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 인덱스 출력
        new_nums = []
        for i in enumerate(nums):
            new_nums.append(i)
        new_nums.sort(key = lambda x : x[1])
        left = 0
        right = len(new_nums) -1
        while left<=right:
            if new_nums[left][1] + new_nums[right][1] == target:
                return [new_nums[left][0], new_nums[right][0]]
            elif new_nums[left][1] + new_nums[right][1] < target:
                left += 1
            else:
                right -= 1