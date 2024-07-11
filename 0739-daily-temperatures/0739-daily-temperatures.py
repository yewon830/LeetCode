class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack = []
        ans = [0]*len(temperatures)
        # stack[-1]과지금 temp를 비교하면서
            # 만약 temp가 크면 계속해서 pop
        #인덱스 정보를 통해 지금 - 이전 의 결과를 ans에 담는다  .
        
        for day,temp in enumerate(temperatures):
            # 스택이 있고 온도 비교를 해서 stack의 마지막보다 지금 온도가 
            while stack and stack[-1][1] < temp:
                prev_day = stack.pop()
                ans[prev_day[0]] = day-prev_day[0]
            
            #stack에 넣기 전에 pop을 해줄 수 있으므로 반복문 이후에
            stack.append((day,temp))
        return ans
            
                
        