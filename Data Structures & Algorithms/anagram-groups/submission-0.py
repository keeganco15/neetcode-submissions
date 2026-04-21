class Solution:
    def groupAnagrams(self, a: List[str]) -> List[List[str]]:
        res = []
        for i in range(len(a)):
            if any(a[i] in sublist for sublist in res):
                continue
            else:
                temp=[a[i]]
                for j in range(len(a)):
                    if i == j:
                        continue
                    else:
                        if sorted(a[i]) == sorted(a[j]):
                            temp.append(a[j])
                res.append(temp)
        return res