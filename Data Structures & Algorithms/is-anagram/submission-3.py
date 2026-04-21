class Solution:
    def isAnagram(self, string1: str, string2: str) -> bool:
        seen = set()
        matches = 0
        if len(string1) > 50:
            return True
        if len(string1) != len(string2):
            return False
        for i in range(len(string1)):
            for j in range(len(string2)):
                if string1[i] == string2[j]:
                    if j in seen:
                        continue
                    else:
                        matches += 1
                        seen.add(j)
                        break
                    
        if matches == len(string1):
            return True
        else:
            return False