class Solution:
    def twoSum(self, a: List[int], t: int) -> List[int]:
        for i in range(len(a)):
            for j in range(len(a)):
                if i == j:
                    continue
                else:
                    if a[i] + a[j] == t:
                        return ([i,j])