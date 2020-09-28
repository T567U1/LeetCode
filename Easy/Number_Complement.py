class Solution:
    def findComplement(self, num: int) -> int:
        # make a list out of num converted to binary
        s = list(bin(num)[2:])
        #replace 1 with zero and vice versa
        for i, x in enumerate(s):
            if x == '1': s[i] = '0'
            else: s[i] = '1'
        return int(''.join(s), 2)

c = Solution()
print(c.findComplement(22))
