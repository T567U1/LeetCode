class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        carry = []
        ans = []

        for i, s in enumerate(S):
            if not carry:
                if ans:
                    ans += len(S[sum(ans):i]),
                else:
                    ans += len(S[0:i]),

            if s not in carry:
                carry.extend([s] * S.count(s))
            carry.remove(s)

        ans += len(S[sum(ans):]),

        return ans[1:]
