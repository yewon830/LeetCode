class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_cnt = 0
        nums_dict = {}
        for num in nums:
            nums_dict[num] = True
        
        for num in nums:
            
            if num-1 not in nums_dict:
                cur_num = num + 1
                cnt = 1
                while cur_num in nums_dict:
                    cnt += 1
                    cur_num += 1
                if max_cnt < cnt:
                    max_cnt = cnt
        return max_cnt
                
            
        
                