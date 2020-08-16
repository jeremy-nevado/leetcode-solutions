class Solution:
    def letterCombinations(self, digits):
        results = []
        mappings = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
            '0': '_'
        }
        results = []
        if not digits:
            return []
        for letter in mappings[digits[0]]:
            results.append(letter)
        for i in range(1, len(digits)):
            digit = digits[i]
            temp = []
            for result in results:
                for letter in mappings[digit]:
                    temp.append(result + letter)
            results = temp
        return results

sol = Solution()
print(sol.letterCombinations('23'))
        
        