class Solution:
    def reverseString(self, s):
        mid = len(s) // 2
        for i in range(0, mid):
            s[i], s[~i] = s[~i], s[i]
