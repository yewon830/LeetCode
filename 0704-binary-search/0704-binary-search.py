
class Solution:
    def search(self, nums: List[int], target: int) -> int:  
        # 재귀 활용하기
        def binarySearch(start,end):
            mid = (start+end)//2
            if start > end:
                return -1
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return binarySearch(mid+1,end)
            else:
                return binarySearch(start,mid-1)
        return binarySearch(0,len(nums)-1)
        
            
        