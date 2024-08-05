from collections import defaultdict
import heapq
import sys
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 다익스트라
        # 모든 노드에 도달하는 최소시간이 다익스트라를 통해서 구할 수 있음
        # 연결 정보 보기 편하게 수정하기
        adjL = defaultdict(list)
        for n1,n2,w in times:
            adjL[n1].append((n2,w))
            
        #최소거리가 들어갈 distance 배열 만들기
        distance = [sys.maxsize]*(n+1) #1부터 시작해서 +1해줌
        heap = [] #우선순위로 가려내기
        heap.append((0,k))
        distance[k] = 0
        while heap:
            cur_dist, cur_v = heapq.heappop(heap)
            print(cur_dist, cur_v)
            for i, w in adjL[cur_v]:
                next_dist = cur_dist + w
                if next_dist < distance[i]:
                    distance[i] = next_dist
                    heapq.heappush(heap,(next_dist, i))
        
        # 0번째 제거
        answer= distance[1:]
        
        if sys.maxsize in answer:
            return -1
        else:
            return max(answer)
        
        
            