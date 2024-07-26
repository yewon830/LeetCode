class Solution:
    def isValid(self, s: str) -> bool:
        #괄호 맞는지 확인
        #여는 괄호면 닫는 괄호 append
        # 닫는 괄호면 pop해주는데  stack 끝이랑 같아야 함
        #아니면 false
        #근데 만약에 스택이 남아있다면 false, 아니면 트루
        
        stack = []
        for i in range(len(s)):
            if s[i] == '(' :
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