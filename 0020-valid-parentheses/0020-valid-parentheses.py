class Solution:
    def isValid(self, s: str) -> bool:
        # 괄호에 맞는지 확인
        # 여는 괄호면 그에 맞는 닫는 괄호를 넣는다
        #닫는 괄호가 나오면 stack의 끝이 그에 맞으편 pop한다, 아니면 false
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