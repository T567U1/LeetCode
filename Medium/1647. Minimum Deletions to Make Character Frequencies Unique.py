class Solution:
    def minDeletions(self, s: str) -> int:
        if len(set(s)) < 2:
            return 0

        ans = []
        tracker = [0] * len(s)
        for i in set(s):
            add = s.count(i)
            if not tracker[add]:
                tracker[add] = i
            else:
                ans += (i, add),

        count = 0
        while ans:
            c, d = ans.pop()
            d1 = d
            while d:
                d -= 1
                count += 1
                if not tracker[d] and d:
                    tracker[d] = c
                    break


        return count
