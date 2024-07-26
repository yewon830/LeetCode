from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        #0번 방에서 시작해서 방을 다 갈 수 있냐 없냐를 불린으로 반환
        queue = deque([0])
        visited = [0]*len(rooms)
        visited[0]=1
        
        while queue:
            current = queue.popleft()
            for i in rooms[current]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = 1
        if all(visited):
            return True
        else:
            return False