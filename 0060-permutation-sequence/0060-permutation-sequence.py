class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        result = []
        arr = []
        k -= 1
        for i in range(1,n+1):
            arr.append(i) 
        # 팩토리얼 계산
        def factorial(n):
            if n == 1 or n== 0:
                return 1
            return n * factorial(n-1)

        for i in range(1,n):
            result.append(arr.pop(k//factorial(n-i)))
            k = k % factorial(n-i)
        result.append(arr.pop())
        
        return ''.join(map(str,result))
                    