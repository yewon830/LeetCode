class Solution:
    def trap(self, height: List[int]) -> int:
        # 투포인터로 풀어보자
        # 좌우에서 이동을 하는데, 왼쪽과 오른쪽을 비교해서 낮은 걸 기준으로 움직인다.
        # 가장 높은 왼쪽, 가장 높은 오른쪽 기준을 세운다
        # 이동하면서, 가장 높은거 - 지금을 cnt에 더한다
        
        left = 0
        right = len(height)-1
        highest_left = height[left]
        highest_right = height[right]
        cnt = 0
        while left < right:
            if height[left] <= height[right]:
                left += 1
                if height[left] > highest_left:
                    highest_left = height[left]
                else:
                    cnt += highest_left - height[left]
            else:
                right -= 1
                # 높이 갱신
                if height[right] > highest_right:
                    highest_right = height[right]
                else:
                    cnt += highest_right - height[right]
        return cnt

            
                    
                    