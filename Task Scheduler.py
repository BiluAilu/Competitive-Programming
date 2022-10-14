import heapq as hq
from collections import Counter, deque
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        count = Counter(tasks)
        max_heap = [-cnt for cnt in count.values()]
        hq.heapify(max_heap)
        queue = deque()
        while max_heap or queue:
            time += 1
            if max_heap:
                cnt = hq.heappop(max_heap) + 1
                if cnt:
                    queue.append([cnt, time+n])
            if queue and queue[0][1] == time:
                hq.heappush(max_heap, queue.popleft()[0])
        return time