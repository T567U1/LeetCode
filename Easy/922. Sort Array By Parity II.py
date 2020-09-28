class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        evens, odds = [], []
        for i in A:
            if i % 2 == 0:
                evens.append(i)
                continue
            odds.append(i)

        rlist = []
        for a, b in zip(evens, odds):
            rlist.append(a)
            rlist.append(b)
