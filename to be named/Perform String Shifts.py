class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        for shif in shift:
            if shif[0]:
                while shif[1] != 0:
                    s = s[-1] + ''.join(list(s)[:-1])
                    shif[1] -=1

            else:
                while shif[1] != 0:
                    s = ''.join(list(s)[1:]) + s[0]
                    shif[1] -=1
        return s
