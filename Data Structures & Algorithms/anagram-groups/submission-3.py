class Solution:
    def groupAnagrams(self, a: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for string in a:
            groups["".join(sorted(string))].append(string)
        return list(groups.values())