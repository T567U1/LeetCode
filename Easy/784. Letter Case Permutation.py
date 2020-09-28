class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        ans = [""]
        for s in S:
            ans = [c + s.lower() for c in ans] + [c + s.upper() for c in ans] if s.isalpha() else [c + s for c in ans]
        return ans
