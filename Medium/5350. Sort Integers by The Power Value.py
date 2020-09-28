class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        dic = {}
        for i in range(lo, hi + 1):
            num = i
            count = 0
            while i != 1:
                if i % 2 == 0:
                    i //= 2
                else:
                    i = 3 * i + 1
                count += 1
            dic[num] = count

        return sorted(dic, key = dic.get)[k - 1]
                    
