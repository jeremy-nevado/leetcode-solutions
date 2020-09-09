class Solution:
    def isIsomorphic(self, s, t):
        if len(s) != len(t): return False
        dict1, dict2 = {}, {}
        for i in range(len(s)):
            if s[i] in dict1.keys():
                if dict1[s[i]] != t[i]:
                    return False
            elif t[i] in dict2.keys():
                if dict2[t[i]] != s[i]:
                    return False
            else:
                dict1[s[i]] = t[i]
                dict2[t[i]] = s[i]
        return True
