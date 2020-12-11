class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            s = float(s)
            return True
        except:
            return False
