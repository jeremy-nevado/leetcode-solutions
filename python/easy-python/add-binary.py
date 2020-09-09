class Solution:
    def addBinary(self, a, b):
        res = ""
        num = str(int(a) + int(b))
        carry = 0
        if "2" not in num:
            return num
        for i in range(len(num) - 1, -1, -1):
            temp = int(num[i]) + carry
            print(temp)
            if temp > 1:
                res = str(temp % 2) + res 
                carry = 1
            else:
                res = str(temp) + res
                carry = 0 
        if carry == 1:
            res = "1" + res
        return res 

sol = Solution()
print(sol.addBinary("1111", "1111"))

            
