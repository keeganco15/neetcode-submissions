class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            stack.append(token)
            if token == "+" or token == "*" or token == "-" or token == "/":
                operator = stack.pop()
                operandA = int(stack.pop())
                operandB = int(stack.pop())
                if operator == "+":
                    stack.append(operandB + operandA)
                if operator == "*":
                    stack.append(operandB * operandA)
                if operator == "/":
                    stack.append(int(operandB / operandA))
                if operator == "-":
                    stack.append(operandB - operandA)
        return int(stack.pop())