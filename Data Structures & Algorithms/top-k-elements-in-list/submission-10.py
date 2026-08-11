from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Keep track of frequency of each number
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
        # Now filled --> 1:1 2:2 3:3
        heap = []
        for key,val in dic.items():
            if len(heap) < k or val > heap[0][0]:
                heapq.heappush( heap, [val,key] )
            if len(heap) > k:
                heapq.heappop(heap)

        fin = []

        for i in range(len(heap)):
            fin.append(heap[i][1])

        return fin
                