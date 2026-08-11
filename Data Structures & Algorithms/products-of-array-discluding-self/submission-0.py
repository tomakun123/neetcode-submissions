class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        skip = 0
        num = 1
        output = []

        while skip < len(nums):
            for i in range(len(nums)):
                if i == skip:
                    continue
                else:
                    num *= nums[i]
            output.append(num)
            skip += 1
            num = 1
        return output
