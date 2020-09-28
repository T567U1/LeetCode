class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        lines = 1
        words = 0
        ord_ = ord('a')

        for i, x in enumerate(S):
            curr = widths[ord(x) - ord_]
            if words + curr < 101:
                words += curr
            else:
                lines += 1
                words = curr

        return [lines, words]
