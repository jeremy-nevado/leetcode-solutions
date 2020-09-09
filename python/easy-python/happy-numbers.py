class Solution:
    def helper(self, n, prev):
        accum = 0
        nums = []
        while n:
            nums.append(n % 10)
            n = n // 10
        for num in nums:
            accum = accum + num ** 2
        if accum == 1:
            return True
        if accum in prev:
            return False
        return helper(accum, prev + [accum])

    def happyNumber(self, n):
        return self.helper(n, [n])

