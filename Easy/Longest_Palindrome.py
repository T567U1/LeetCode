class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd, count, sets =  0, 0, set(s)
        for ele in sets:
            # counts exiting elements on s
            num = s.count(ele)
            #if nums % 2 counts is added number of existing elements
            if bool(num % 2 == 0): count += num
            else:
                count += num -1
                odd = 1
        return count + odd

c = Solution()
print(c.longestPalindrome('adam'))
