class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        if sum(A) % 3:
            return False
        thrid = sum(A) / 3
        res, anchor = [], 0
        for i in range(len(A)):
            if len(res) == 2:
                res.append(A[i:])
                break
            elif sum(A[anchor: i]) == thrid:
                res.append(A[anchor: i])
                anchor = i


        return len(res) == 3
