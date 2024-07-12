class Solution:
    def isValid(self, s: str) -> bool:
        # 짝을 맞춘다.
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(')')
            elif s[i] == '[':
                stack.append(']')
            elif s[i] == '{':
                stack.append('}') 
            elif stack and stack[-1] == s[i]:
                    stack.pop()
            else:
                return False
        if stack:
            return False
        else:
            return True