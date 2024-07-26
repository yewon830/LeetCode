from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        #모든 노드를 살펴본다.  
        #나와 연결된 친구가 나랑 다른 팀이여야 한다
        # 미할당 0, A는 1, B는 2이다.
        # 미할당이면 나랑 반대로 넣는다
        # 할당인데 나랑 같으면 바로 False
        answer = True
        visited= [0]*len(graph)
        
        def bfs(num):
            queue = deque()
            queue.append(num)
            visited[num] = 1
            while queue:
                cur = queue.popleft()
                for i in graph[cur]:
                    if not visited[i]:
                        if visited[cur] == 1:
                            visited[i] = 2
                        elif visited[cur] == 2:
                            visited[i] = 1
                        queue.append(i)
                    else:
                        if visited[cur] == visited[i]:
                            return False
            return True
        
        for i in range(len(graph)):
            if not visited[i] and not bfs(i):
                return False
        return True
                    
                    
                
                