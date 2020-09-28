class Fenwick:
    def __init__(self, n):
        self.a = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.a[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i < len(self.a):
            self.a[i] += x
            i += i & -i

class Solution:
    def minInteger(self, num, K):
        A = list(map(int, num))
        N = len(A)

        indexes = [[] for _ in range(10)]
        for i, d in enumerate(A):
            indexes[d].append(i)

        for row in indexes:
            row.reverse()

        # indexes = [[], [3], [2], [1], [0], ...]

        fen = Fenwick(N + 1)
        ans = []
        while K:
            for d in range(10):
                row = indexes[d]
                if not row:
                    continue

                j = row[-1]
                rank = j - fen.sum(j + 1)
                if rank <= K:
                    K -= rank
                    ans.append(d)
                    row.pop()
                    fen.add(j + 1, 1)
                    break
            else:
                break

        stuff = []
        for d, row in enumerate(indexes):
            for i in row:
                stuff.append([i, d])
        stuff.sort()
        for i, d in stuff:
            ans.append(d)

        return "".join(map(str, ans))
