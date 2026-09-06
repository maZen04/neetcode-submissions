class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        import math
        stack = []
        operators = {'+','-','/','*'}
        for i in tokens:
            if i in operators:
                x = stack.pop()
                y = stack.pop()
                if i == '+':
                    stack.append(x+y)
                elif i == '-':
                    stack.append(y-x)
                elif i == '*':
                    stack.append(x*y)
                elif i == '/':
                    stack.append(int(y/x))
            else:
                stack.append(int(i))
        return stack[0]