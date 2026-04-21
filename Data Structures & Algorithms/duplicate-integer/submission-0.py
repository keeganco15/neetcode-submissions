class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j == i: #skip same index to avoid false diplication tracking
                    continue
                else:
                    if nums[i] == nums[j]: 
                        return True
        return False