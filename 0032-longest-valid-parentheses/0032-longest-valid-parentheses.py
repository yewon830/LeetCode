class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # 가장 긴 유효한 괄호 찾기
        # -1, 그리고 잘못된 괄호를 기준점으로 삼는다.
        # 여는 괄호면 스택에 일단 인덱스를 넣는다
        # 닫는 괄호면은 일단 pop한다
        # pop하는데, 만약에 스택이 있으면 longest를 기준점이랑 인덱스를 빼서 더 큰걸로 업데이트한다
        # 스택이 없으면 인덱스 어팬드
        
        stack = [-1]
        longest = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    longest = max(longest, i-stack[-1])
                else:
                    stack.append(i)
        return longest