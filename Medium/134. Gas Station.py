class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        a, b = [0] * len(gas), [0] * len(gas)
        for i, (x, y)  in enumerate(zip(gas, cost)):
            a[i] = x - y
            b[i] = sum(a[:i + 1])

        if sum(a) < 0:
            return -1

        ans = b.index(min(b)) + 1
        return ans if ans < len(gas) else 0
