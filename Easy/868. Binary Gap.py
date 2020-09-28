class Solution:
    def binaryGap(self, N: int) -> int:
        ans = []
        N = bin(N)[2:]
        for i, x in enumerate(N):
            if x == '1':
                if '1' in N[:i][::-1]:
                    ans.append(N[:i][::-1].index('1') + 1)
        return max(ans) if ans else 0
