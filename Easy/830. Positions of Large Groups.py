class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        ans = []
        count = 0

        for i, x in enumerate(S):
            if x != S[i - 1]:
                if count > 2:
                    ans.append([i - count, i - 1])
                count = 0
            count += 1

        if count > 2:
            ans.append([len(S) - count, len(S) - 1])

        return ans
