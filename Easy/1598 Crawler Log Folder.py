class Solution:
    def minOperations(self, logs: List[str]) -> int:
        r = 0
        for i in logs:
            if i == '../':
                r -= 1 if r > 0 else 0
            elif i == './':
                r += 0
            else:
                r += 1

        return r if r > 0 else 0
