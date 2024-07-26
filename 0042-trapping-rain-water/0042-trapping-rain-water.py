class Solution:
    def trap(self, height: List[int]) -> int:
        # 투 포인터로 이도ㅓㅇ
        # 왼,오 기준에서 작은걸 기준으로 움직이기
        # 최대 높이랑 비교하면서 차이 계산
        
        left = 0
        right = len(height)-1
        top_left = height[left]
        top_right = height[right]
        cnt = 0
        while left<right:
            if height[left] <= height[right]:
                if top_left < height[left]:
                    top_left = height[left]
                else:
                    cnt += top_left - height[left]
                left += 1
            else:
                if top_right < height[right]:
                    top_right = height[right]
                else:
                    cnt += top_right - height[right]
                right -= 1
        return cnt

            
                    
                    