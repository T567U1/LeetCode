class Solution:
    def arrangeWords(self, text: str) -> str:
        text = text.split()
        count = '@'
        ans = {}
        for i, x in enumerate(text):
            if x.lower() in ans:
                ans[str(count) + x.lower()] = len(x)
                count += '@'
            ans[x.lower()] = len(x)
        return ' '.join(sorted(ans, key = ans.get)).capitalize().replace('@', '')
