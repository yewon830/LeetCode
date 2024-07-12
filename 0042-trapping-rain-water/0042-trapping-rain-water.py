class Solution:
    def trap(self, height: List[int]) -> int:
        # 투포인터로 풀어보자
        left = 0
        right = len(height)-1
        rain = 0
        highest_left = height[left] 
        highest_right = height[right]
        while(left<right):
            # 더 낮은 기둥을 기준으로 물을 채울 수 있다
            #왼쪽 벽이 더 낮음
            if height[left]<= height[right]:
                left += 1
                if highest_left > height[left]:
                    rain += highest_left - height[left]
                else:
                    highest_left = height[left]
            else:
                right -= 1
                if highest_right > height[right]:
                    rain += highest_right - height[right]
                else:
                    highest_right = height[right]
        return rain
                    
                    