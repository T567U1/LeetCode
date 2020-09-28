class Solution:
    def simplifyPath(self, path: str) -> str:
        ans = []
        path = path.split('/')
        for s in path:
            if s == "..":
                if ans:
                    ans.pop()
            else:
                if s.isalpha() or '_' in s:
                    ans += s,
                elif '.' in s:
                    t = s.replace('.', '')
                    if t or s.count('.') > 2:
                        ans += s,

        return '/' + '/'.join(ans)
                
