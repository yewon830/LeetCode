from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # 노드로 이동하기
        #0번째 방에서 시작해서 이동
        queue = deque()
        queue.append(rooms[0])
        visited = [0]*len(rooms)
        visited[0] = 1
        while queue:
            cur = queue.popleft()
            if cur:
                for i in cur:
                    if not visited[i]:
                        visited[i] = 1
                        queue.append(rooms[i])
        if 0 in visited:
            return False
        else: 
            return True
