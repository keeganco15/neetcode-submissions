class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += str(len(string)) + "#"
            for char in string:
                encoded += chr(ord(char)+1)
        return encoded

    def decode(self, strs: str) -> List[str]:
        res = []
        i = 0
        while i < len(strs):
            j = i
            while strs[j] != "#":
                j += 1

            length = int(strs[i:j])

            i = j + 1

            shiftedStr = strs[i:i+length]
            original = ""
            for char in shiftedStr:
                original += chr(ord(char)-1)
            res.append(original)
            i += length
        return res