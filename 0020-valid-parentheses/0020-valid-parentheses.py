class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        #s에 있는걸 pop한다
        
#         pop해서 나오는거랑 지금거랑 맞아야 함.
        for i in range(len(s)):
            # 여는 괄호 없이 닫는 괄호만 나오는 경우 
            if not stack and (s[i] == ')'or s[i] == '}' or s[i]== ']'):
                return False
            
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i]) 
            if s[i] == ')':
                if stack[-1] =='(':
                    stack.pop()
                else:
                    return False
            elif s[i] == ']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            elif s[i] == '}':
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return False

        
        if stack:
            return False
        else:
            return True
            
            
            
            
            
        
        
                
            
            