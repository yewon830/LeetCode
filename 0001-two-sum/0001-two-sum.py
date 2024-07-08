class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 두개 더해서 target되는 값 찾기
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if(nums[i]+ nums[j] == target):
                    return [i,j]
        
                
                
                
            
        