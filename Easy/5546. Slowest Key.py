class Solution:
    def slowestKey(self, r: List[int], k: str) -> str:
        ans = {r[0]: [k[0]]}
        for i, (time, key) in enumerate(zip(r[1:], k[1:])):
                t = time - r[i]
                if t in ans:
                    ans[t] += key,
                else:
                    ans[t] = [key]

        return sorted(ans[max(ans)])[-1]
