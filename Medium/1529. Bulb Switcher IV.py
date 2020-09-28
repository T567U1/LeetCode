class Solution:
    def minFlips(self, target: str) -> int:
        if len(set(target)) == 1:
            return target[0]

        start = target[target.index('1'):]
        count, flag = 0, 0

        for i, x in enumerate(start):
            if flag == x:
                continue
            flag = x
            count += 1

        return count
