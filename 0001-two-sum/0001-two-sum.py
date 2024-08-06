class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 해시 테이블로 풀기
        # nums 값:인덱스 인 딕셔너리 추가로 만들기
        # for문으로 nums을 돌면서, target - 지금요소 가 있는지 딕셔너리에서 확인
        nums_dict = {}
        for i,e in enumerate(nums):
            nums_dict[e] = i
        
        print(nums_dict)
        
        for i in range(len(nums)):
            if (target-nums[i]) in nums_dict and i !=nums_dict[target-nums[i]]:
                return [i, nums_dict[target-nums[i]]]
