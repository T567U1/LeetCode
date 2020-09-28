class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False

        n = len(A)
        i = 0
        while i < n-1 and A[i+1] > A[i]:
            i += 1

        if i == 0 or i == n-1:
            return False

        while i < n-1 and A[i+1] < A[i]:
            i += 1

        return i == n-1
