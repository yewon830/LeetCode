class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        #전체 순열에서 n번째 순열에 어떤 수가 들어가는지 찾기.
        # 그러기 위해서는 인덱스가 어디 집단에 있어서 무슨 수가 들어가는지 유추 필요함. 
        # 1. k // (n-1)! 해서 집단을 알아내고, 그리고 그걸 인덱스에 넣는다
        # 2. k = k%(n-1)!로 재할당하고, 계속 반복한다. (아웃풋 길이가 n이 될떄까지)
        
        #반복문으로 풀기
        result = []
        k -= 1
        nums = [num for num in range(1,n+1)]
        def factorial(n):
            if n==1 or n==0:
                return 1
            return n * factorial(n-1)
        i =1
        while(i<=n):
            idx = k // factorial(n-i)
            num  = nums.pop(idx)
            result.append(num)
            k = k % factorial(n-i)
            i += 1
        
        return ''.join(map(str,result))
        
            