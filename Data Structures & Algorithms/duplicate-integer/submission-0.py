class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = []
        for i in range(len(nums)):
            if nums[i] not in check:
                check.append(nums[i])
            else:
                return True
        return False