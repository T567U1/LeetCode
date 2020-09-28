class Solution:
    def calPoints(self, ops: List[str]) -> int:
        result = []

        for i in ops:
            if i == 'C':
                 result.pop()
            elif i == 'D':
                result.append(int(result[-1] * 2))
            elif i == '+':
                result.append(result[-1] + result[-2])
            else:
                result.append(int(i))

        return sum(result)
