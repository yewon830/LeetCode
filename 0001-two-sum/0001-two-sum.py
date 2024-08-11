class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 해시 테이블로 풀기
        # 두 요소 합을 더하면 target이 되어야 한다. 
        nums_dict = {}
        for i,e in enumerate(nums):
            if target - e in nums_dict:
                return [i, nums_dict[target-e]]
            nums_dict[e] = i
        
