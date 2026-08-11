from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Keep track of frequency of each number
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
        
        # Ex 1: dic[key:value] = { 1:1, 2:2, 3:3 }
        # Use a heap to sort --> [[key,value],...] format
        # 3:1 0:2 1:1
        heap = []
        for key, val in dic.items():
            if k > len(heap) or val > heap[0][0]:
                heapq.heappush(heap, [val, key])
            if k < len(heap):
                heapq.heappop(heap)
        
        final = []
        for i in range(k):
            final.append(heap[i][1])
        return final
                