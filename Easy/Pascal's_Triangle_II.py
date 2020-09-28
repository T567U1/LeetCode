class Solution(object):
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            list = [1]
            return list
        list = [[1]]
        for i in range(1, rowIndex + 1):
            list1 = []
            for x in range(i + 1):
                if x == 0 or x == len(list[i-1]):
                    list1.append(1)
                    continue
                else:
                    list1.append(list[i-1][x-1] + list[i-1][x])
            list.append(list1)
        return list[rowIndex]

c = Solution()
print(c.generate(3))
