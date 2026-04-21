class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += str(len(string)) + "#"
            for char in string:
                encoded += chr(ord(char)+1)
        return encoded

    def decode(self, strs2: str) -> List[str]:
        res = []
        temp = ""
        lengthStr = ""
        length = 0
        currentIndex = 0

        while currentIndex < len(strs2):
            if 47 < ord(strs2[currentIndex]) < 58:
                lengthStr += strs2[currentIndex]
                currentIndex += 1
                if strs2[currentIndex] == "#":
                    length = int(lengthStr)
                    currentIndex += 1
                    for i in range(currentIndex, length+currentIndex):
                        temp += chr(ord(strs2[currentIndex])-1)
                        currentIndex += 1
                    res.append(temp)
                    length = 0
                    lengthStr = ""
                    temp = ""
        
        return res