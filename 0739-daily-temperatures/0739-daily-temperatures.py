class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #나보다 높은 온도를 만나기까지 얼마나 걸리는가?
        # 인덱스를 저장하면서, 
        # stack끝보다 높은 온도면은 pop
        
        stack = []
        answer = [0]*len(temperatures)
        for day,temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                prev_day, prev_temp = stack.pop()
                answer[prev_day] = day - prev_day
            stack.append((day,temp))
        return answer
                
        