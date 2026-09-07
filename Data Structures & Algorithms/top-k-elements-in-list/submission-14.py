from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f = defaultdict(int)
        # step 1: get a frequency dict of elements
        for number in sorted(nums):
            if number not in f:
                f[number] = 1
            else:
                f[number] += 1
        
        # step 2: retrieve k highest frequency
        final = []
        for i in range(k):
            high = max(f.values())
            for num in f:
                if f[num] == high:
                    final.append(num)
                    f[num] = -1
                    break

        return final