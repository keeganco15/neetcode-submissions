class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sortedA = sorted(set(nums))
        res = 0
        temp = 0
        direction = ""
        for i in range(len(sortedA)):
            if temp == 1:
                if sortedA[i-1] == sortedA[i]-1:
                    direction = "up"
                else:
                    direction = "down"
                
            if sortedA[i-1] != sortedA[i]-1 and direction == "up":
                temp = 0
        
            elif sortedA[i-1]+1 != sortedA[i] and direction == "down":
                temp = 0
            temp += 1
            if temp > res:
                res = temp
        return res
