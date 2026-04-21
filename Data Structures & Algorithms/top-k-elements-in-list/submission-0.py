class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = {}
        for num in nums:
            numCount[num] = numCount.get(num, 0) + 1
        return list([key for key, value in sorted(numCount.items(), key=lambda item: item[1], reverse=True)[:k]])