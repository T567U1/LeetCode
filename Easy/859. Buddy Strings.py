class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B) or not A or not B:
            return False
        t_a = list(A)
        if A[::-1] == B or B[::-1] == A:
            return True
        for i, (a,b) in enumerate(zip(A, B)):
            if a != b:
                t_a[i], t_a[i + 1] = t_a[i + 1], t_a[i]
                return ''.join(t_a) == B
        return len(A) > 2 and len(set(list(A))) != len(B
