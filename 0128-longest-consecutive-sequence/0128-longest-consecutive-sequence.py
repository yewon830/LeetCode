class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 가장 긴 연속 길이 
        # 접근 방법
        #   해시 테이블을 만들어서 연속한 수를 센다. 
            # 나 기준 -1 인 녀석이 해시테이블에 없다면
                # cnt = 1로 갱신
                # target을 나로 갱신
                # 만약에 해시테이블에 target+1이 있다면 그동안
                    # cnt ++
                    # target ++
        
        max_cnt = 0
        nums_dict = {}
        for num in nums:
            nums_dict[num] = True
        
        for num in nums:
            if num-1 not in nums_dict: #이전 연속하는 수가 없을때
                cnt = 1
                target = num
                while target+1 in nums_dict:
                    cnt += 1
                    target += 1
                if cnt > max_cnt:
                    max_cnt = cnt
        return max_cnt
                
            
        
                