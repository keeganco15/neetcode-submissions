class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {"(" : ")", "[" : "]", "{" : "}"}

        for char in s:
            if char in mapping.keys():
                stack.append(char)
            else:
                if not stack or char != mapping[stack[-1]]:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0
