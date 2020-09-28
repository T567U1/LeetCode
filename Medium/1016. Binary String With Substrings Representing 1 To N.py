class Solution:
    def queryString(self, S: str, N: int) -> bool:
        for x in range(1, N + 1):
            if bin(x)[2:] not in S:
                return False

        return True
