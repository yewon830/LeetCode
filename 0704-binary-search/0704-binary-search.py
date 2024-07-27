class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        #반 쪼갈라서 찾기
        #이미 정렬 되어있지
        start = 0
        end = len(nums)-1
        while start<=end:
            mid = (start+end)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] <target:
                start = mid+1
            else:
                end = mid -1
        return -1
        
        