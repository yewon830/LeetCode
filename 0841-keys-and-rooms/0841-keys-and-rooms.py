class Solution(object):
    def canVisitAllRooms(self, rooms):
        #일단 시작은 무조건 0번방에서 시작.
        # 이걸 그래프로 생각하면 인접리스트와 비슷해보인다.
        # DFS나 BFS로 풀 수 있을 듯
        stack = [0]
        visited = [0]*len(rooms)
        visited[0] = 1
        while stack:
            current = stack.pop()
            if rooms[current]:
                for i in rooms[current]:
                    if not visited[i]:
                        visited[i] = 1
                        stack.append(i)
        
        if 0 in visited:
            return False
        else:
            return True
