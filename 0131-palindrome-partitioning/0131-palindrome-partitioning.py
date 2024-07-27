class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # 회문인 거 모음
        # 슬라이싱 범위를 조정.
        result = []
        def backTracking(start,path):
            
            if start == len(s):
                result.append(path[:])
                return
            
            for i in range(start+1, len(s)+1):
                char = s[start:i]
                if char == char[::-1]:
                    path.append(char)
                    backTracking(i, path)
                    path.pop()
        backTracking(0,[])
        return result
                
                
            