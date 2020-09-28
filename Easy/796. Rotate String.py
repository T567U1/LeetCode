class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        for index in range(len(A) + 1):
            if B[index:] + B[:index] == A:
                return True
        return False
