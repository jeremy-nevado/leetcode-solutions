class Solution:
    def backtrack(self, s, wordDict, index):
        for i in range(index, len(wordDict)):
            if s == "" :
                return True
            word = wordDict[i]
            if word in s:
                temp = s.replace(word, "")
                if temp == "":
                    return True
                else:
                    return self.backtrack(temp, wordDict, index + 1)
            else:
                return self.backtrack(s, wordDict, index + 1)
        return

    def wordBreak(self, s, wordDict):
        '''
        s is a non-empty string
        wordDict is a dictionary containing a list of non-empty words
        determines if s can be segmented into a space-separated sequence of one or more dictionary words.
        '''
        return self.backtrack(s, wordDict, 0)

