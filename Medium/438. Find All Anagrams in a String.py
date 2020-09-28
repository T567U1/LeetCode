class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        ref = collections.defaultdict(int)

        for c in p:
            ref[c] += 1

        i, j = 0, 0
        missing = len(p)

        while j < len(s):
            if ref[s[j]] > 0:
                missing -= 1

            ref[s[j]] -= 1

            while not missing:
                if j - i + 1 == len(p):
                    ans.append(i)

                if ref[s[i]] >= 0:
                    missing += 1

                ref[s[i]] += 1
                i += 1

            j += 1

        return ans
