class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        A, res = ''.join(map(str, A)), []
        for i in range(len(A)):
            res.append(int(''.join(A[:i + 1]), 2) % 5 == 0)


        return res
