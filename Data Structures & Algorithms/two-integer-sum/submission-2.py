class Solution:
    def twoSum(self, a: List[int], t: int) -> List[int]:
        dic = {}
        for i in range(len(a)):
            if t - a[i] in dic:
                return [dic[t-a[i]], i]
            else:
                dic[a[i]] = i