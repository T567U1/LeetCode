class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if k > len(s) or len(s) == 1 and '0' not in s:
            return False
        S = '{:00' + str(k) + 'b}'  if k < 10 else '{:0' + str(k) + 'b}'
        i = 0
        while len(bin(i)[2:]) <= k:
            if S.format(i) not in s:
                return False
            i += 1
        return True
