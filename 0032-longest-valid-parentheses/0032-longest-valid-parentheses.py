class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # 가장 긴 유효 괄호 찾기
        # 가장 긴 유효 괄호 찾는 법 : -1과 잘못된 괄호를 기준점으로 해서 그 간격 재기
        # 여는 괄호면 append(인덱스를)
        # 닫는 괄호면 pop
            # 스택이 있으면 , stack[-1]과 지금 인덱스를 빼고 갱신
            # 스택이 없으면. 지금 인덱스 append
        longest = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    longest = max(longest, i - stack[-1])
                else:
                    stack.append(i)
        return longest