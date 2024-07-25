class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #나보다 높은 온도를 만나기까지 걸리는 시간은?
        #스택에 인덱스까지 넣어준다
        # 인덱스에 나중-지금을 넣어주면서, 
        # stack[-1]보다 큰 값이 나오면 들어있는걸 pop한다
        
        stack = []
        answer = [0] * len(temperatures)
        for day,temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                prev_day, prev_temp = stack.pop()
                answer[prev_day] = day - prev_day
            stack.append((day,temp))
        return answer
        