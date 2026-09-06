class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {')':'(',']':'[','}':'{'}
        for i in s:
            if i not in parentheses:
                stack.append(i)
            else:
                if not stack or stack.pop() !=  parentheses[i]:
                    return False
        if len(stack)==0:
            return True
        else:
            return False