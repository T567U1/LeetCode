class Solution:
    def countSegments(self, s: str) -> int:
        if not s or len(s.strip()) == 0: return 0
        s = list(s.split(' '))
        while '' in s:
            s.remove('')
        return len(s)
        #len(s.strip()) works too...... 
