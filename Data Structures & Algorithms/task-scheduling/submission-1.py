"""
# get the character with the most frequency and plan the other characters around that
# to constantly get the character with the highest frequency, we can use a maxHeap
# And we can use a queue to triage

"""
from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        counts = Counter(tasks)
        maxHeap = [count for count in counts.values()]  # [3, 3]
        heapq.heapify_max(maxHeap)
        print(maxHeap)
        q = deque()     # (task, next_time)
        time = 0

        while maxHeap or q:
            time += 1
            if maxHeap:
                topTask = heapq.heappop_max(maxHeap) - 1
                if topTask:
                    q.append((topTask, time + n))
            if q and q[0][1] == time:
                q_left = q.popleft()[0]
                heapq.heappush_max(maxHeap, q_left)
            
        return time
