class Solution(object):
    def romanToInt(self, s):
         roman_to_Dec = 0
         roman_Numbers = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
         }
         for char in range(len(s)):
             print(roman_to_Dec)
             print(s[char])
             if char != 0 and roman_Numbers[s[char]] > roman_Numbers[s[char - 1]]:
                 print("pass")
                 roman_to_Dec += roman_Numbers[s[char]] - roman_Numbers[s[char - 1]] - roman_Numbers[s[char - 1]]

             else:
                 roman_to_Dec += roman_Numbers[s[char]]

         return roman_to_Dec


cl = Solution()
print(cl.romanToInt('MCMXCIV'))
