class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(start,end):
            if start>end:
                return -1
            mid = (start+end)//2
            if nums[mid]==target:
                return mid
            elif nums[mid] < target:
                return binarySearch(mid+1, end)
            else:
                return binarySearch(start, mid-1)
                
                
        result = binarySearch(0, len(nums)-1)
        return result