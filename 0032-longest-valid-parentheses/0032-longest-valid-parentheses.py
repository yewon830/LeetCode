class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # 가장 유효한 괄호 길이 찾기
        # 찾는 법 : 처음은 -1로, 그리고 유효하지 않은 괄호를 기준점으로 삼아서 인덱스 뺴주기
        #여는 괄호면 일단 인덱스를 넣는다
        # 닫는 괄호가 나오면 pop
        #스택이 있으며ㅑㄴ, 지금 인덱스 - stack[-1]을 한다. ->  longest
        #pop하다가 스택이 비었다면, 그건 잘못된 것이므로 인덱스를 새로 넣는다.
        
        stack = [-1]
        longest = 0
        for i,c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    longest = max(longest,i - stack[-1])
                else:
                    stack.append(i)
        return longest