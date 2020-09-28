class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        a, b = A.split(), B.split()
        A, B = set(A.split()), set(B.split())
        ans = list(A.difference(B)) + list(B.difference(A))
        ans_t = list(A.difference(B)) + list(B.difference(A))
        for word in ans_t:
            if a.count(word) > 1 or b.count(word) > 1:
                ans.remove(word)
        return ans
        
