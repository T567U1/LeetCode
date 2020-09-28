class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted([abs(i * i) for i in A])
