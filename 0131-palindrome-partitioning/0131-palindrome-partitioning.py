class Solution:
    def partition(self, s):
        result = []
        def backTracking(start, partitions ):
            if start == len(s):
                result.append(partitions[:])
                return
            
            # 이 부분이 슬라이싱 범위를 추가해주는 부분
            for i in range(start+1, len(s)+1):
                chars = s[start:i]
                # 회문 검사
                if chars == chars[::-1]:
                    partitions.append(chars)
                    backTracking(i,partitions)
                    partitions.pop()
        backTracking(0,[])
        return result