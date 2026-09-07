import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while stones:
            # print("stones before y pop: ")
            # print(stones)

            y = heapq.heappop_max(stones)
            # print(f"stones after y pop ({y}): ")
            # print(stones)

            if stones:
                x = heapq.heappop_max(stones)
                # print(f"stones after x pop ({x}): ")
                # print(stones)
            else:
                return y

            
            if y == x:
                continue
            else:
                heapq.heappush_max(stones, y - x)
        
        return 0
        