from collections import deque, defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # indegree 기록한다.
        
        indegree = [0]*numCourses
        adjL = defaultdict(list)
        visited = [0]*numCourses
        
        for n1,n2 in prerequisites:
            indegree[n2] += 1
            adjL[n1].append(n2)
     
        queue = deque()
        
        flag = False
        for i in range(len(indegree)):
            if indegree[i] == 0:
                flag = True
                queue.append(i)
                visited[i] = 1
        if not flag:
            return False
        
        
        #인디그리가 0인걸로 시작해서 탐색하면서 1씩 줄이기
        while queue:
            cur_node = queue.popleft()
            flag = True
            for v in adjL[cur_node]:
                # 방문 안했다면 거기 인디그리 줄이기
                if not visited[v] and indegree[v]:
                    indegree[v] -= 1    
                if not visited[v] and indegree[v] == 0:
                    queue.append(v)
                    visited[v] = 1
                
        #방문 덜했으면 
        for i in visited:
            if i==0:
                return False
        return True
            
            
            
            
        
            
            
            
        