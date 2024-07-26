class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 순열, 들어갔던게 또 들어갈 수 있음.
        result = []
        def perm(path):

            if len(path) == len(nums):
                result.append(path[:])
                return
            
            for i in range(len(nums)):
                if nums[i] not in path:
                    path.append(nums[i])
                    perm(path)
                    path.pop()
        
        perm([])
        return result