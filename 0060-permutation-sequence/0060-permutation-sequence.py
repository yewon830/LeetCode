class Solution:
    def getPermutation(self, n: int, k: int) -> str:
#         1. 팩토리얼을 계산한다. k는 하나 뺴준다(인덱스라서)
# 2. 반복문으로 k//(n-i)를 구하고,
#    k 에 k%(n-i)값을 할당한다.
        k -= 1
        result = []
        nums = [i for i in range(1,n+1)]
        def factorial(n):
            if n == 1 or n== 0:
                return 1
            return n * factorial(n-1)
        
        for i in range(1,n+1):
            result.append(nums.pop(k//factorial(n-i)))
            k = k % factorial(n-i)
        
        return ''.join(map(str,result))
    