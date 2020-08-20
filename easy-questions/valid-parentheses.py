class Solution:
    def isValid(self, s):
        pairs = []
        if not s:
            return True
        for char in s:
            if char == '(' or char == '{' or char == '[':
                pairs.append(char)
            elif char == ')':
                if pairs.pop() != '(':
                    return False
            elif char == '}':
                if pairs.pop() != '{':
                    return False
            elif char == ']':
                if pairs.pop() != '[':
                    return False
        if pairs:
            return False
        return True
sol = Solution()
print(sol.isValid('('))

