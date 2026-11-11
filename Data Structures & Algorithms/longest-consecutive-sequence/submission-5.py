class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        long = 1
        curr = 1
        if len(nums) == 0:
            return 0
        for num in nums:
            n = num
            if (n-1) in nums:
                continue
            while (n+1) in nums:
                curr += 1
                n += 1
            if curr > long:
                long = curr
            curr = 1
                
        return long   
        
             