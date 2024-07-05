class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 두 수의 합이 타겟이 되는 수들의 인덱스 반환
        # 투 포인터 사용하기, (정렬기본)
        left = 0
        right = len(nums)-1
        new_nums = list(enumerate(nums))
        new_nums.sort(key = lambda x : x[1])
        while left<=right:
            if new_nums[left][1] + new_nums[right][1] == target:
                return [new_nums[left][0], new_nums[right][0]]
            elif new_nums[left][1] + new_nums[right][1] < target:
                left += 1
            else:
                right -= 1
        
                
                
                
            
        