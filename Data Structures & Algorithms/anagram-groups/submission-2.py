class Solution:
    def groupAnagrams(self, a: List[str]) -> List[List[str]]:
        dic = {}
        for string in a:
            dic.setdefault("".join(sorted(string)), []).append(string)
        return list(dic.values())