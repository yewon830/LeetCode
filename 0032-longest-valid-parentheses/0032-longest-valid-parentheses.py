class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # 스택에 기준점을 세우고, 그걸 기준으로 유효하면 계속 길이 추가, 아니면 새로 기준점 세우기
        longest = 0
        stack = [-1] #스택에 인덱스를 넣어준다. 시작점은 0이전인 -1
        for i in range(len(s)):
            if s[i] == '(':
                #여는 괄호라면 인덱스 append
                stack.append(i)
            else:
                stack.pop() #유효 여부와 상관없이 pop
                if not stack: #스택이 비었으면 기준 점 넣어두기
                    stack.append(i)
                else: # 기준점으로 비교
                    longest = max(longest, i - stack[-1])
        return longest
        