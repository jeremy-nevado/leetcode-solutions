class Solution:
    def decodeString(self, s):
        lst = s.split(']')
        for i in range(len(lst)):
            lst[i] = lst[i].split('[')
        print(lst)


sol = Solution()
sol.decodeString('abc3[cd]xyz')
sol.decodeString('3[a2[c]]')
sol.decodeString('2[abc]3[cd]ef')
