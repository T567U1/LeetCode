class Solution(object):
    def reformat(self, s):
        A, B = [], []
        for c in s:
            if c.isalpha():
                A.append(c)
            else:
                B.append(c)

        if len(A) < len(B):
            A, B = B, A

        ans = []
        while A and B:
            ans.append(A.pop())
            ans.append(B.pop())
        if A:
            ans.append(A.pop())
        return "" if A else "".join(ans)


        
