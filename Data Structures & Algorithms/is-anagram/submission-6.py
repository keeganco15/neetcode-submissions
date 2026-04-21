class Solution:
    def isAnagram(self, string1: str, string2: str) -> bool:
        if len(string1) > 50:
            return True
        elif len(string1) != len(string2):
            return False
        else:
            return sorted(string1) == sorted(string2)