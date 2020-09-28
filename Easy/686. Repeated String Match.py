'''
Solucion by user https://leetcode.com/hramireddy1/
class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        for i in range(1,abs(len(B)-len(A))+3):
            if((A*i).count(B)>0):
                return i
        return -1
'''




class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        s = A
        while B not in A:
            A += s
            if len(B) * 2 <= len(A) and B not in A:
                return -1

        return A.count(s)
