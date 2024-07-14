from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # 집합 A,B 두개로 나눠서 a요소-b요소끼리 연결이 모두 되어있나 확인
        # 지금 방문했을 때, 연결 되어있는 녀석들은 다른 집합에 들어가야 한다.
        
        # -1을 미할당, 0을 A, 1을 B
        check = [-1 for _ in range(len(graph))] 
        for i in range(len(check)):
            if check[i] == -1:
                queue = deque([i])
                check[i] = 0
                while queue:
                    current = queue.popleft()
                    for j in graph[current]:
                        if check[j] == -1:
                            if check[current] == 0:
                                check[j] = 1
                            elif check[current] ==1 :
                                check[j] = 0
                            queue.append(j)
                        elif check[current] == check[j]:
                            return False
        return True