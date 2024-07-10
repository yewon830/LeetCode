class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #  투 포인터로 풀기
        # 투 포인터로 풀기 위해서는 정렬이 필요한데, 정렬해버리면 원래 인덱스 값의 정보가 없어지므로
        # enumerate로 인덱스 값을 남겨준다
        new_nums = [i for i in enumerate(nums)]
        
        #정렬(1번째 키 기준)
        new_nums.sort(key= lambda x : x[1])
        
        #투포인터 0이 인덱스 1이 값
        left = 0
        right = len(new_nums)-1
        while(left<=right):
            if new_nums[left][1] + new_nums[right][1] == target:
                return [new_nums[left][0], new_nums[right][0]]
            elif new_nums[left][1] + new_nums[right][1] < target:
                left += 1
            else:
                right -= 1
            
                
        
                
                
                
            
        